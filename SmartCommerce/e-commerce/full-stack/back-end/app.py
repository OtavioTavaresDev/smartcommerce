from flask import Flask, jsonify, request
from flask_cors import CORS
from database import SessionLocal, engine
from models import Product, Base, User, Order
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

SECRET_KEY = "super-secret-key"

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
CORS(app, supports_credentials=True, origins=["http://localhost:5500", "http://127.0.0.1:5500"])

# Criar tabelas
Base.metadata.create_all(bind=engine)

# ================= DECORATOR DE TOKEN =================

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({"error": "Token mal formatado"}), 401
        
        if not token:
            return jsonify({"error": "Token ausente"}), 401
        
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = decoded["user"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated

# ================= HOME =================

@app.route("/")
def home():
    return {"message": "API rodando"}

# ================= REGISTER =================

@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        db = SessionLocal()
        
        existing = db.query(User).filter_by(username=data["username"]).first()
        if existing:
            db.close()
            return jsonify({"error": "Usuário já existe"}), 400
        
        hashed = generate_password_hash(data["password"])
        
        user = User(
            username=data["username"],
            password=hashed
        )
        
        db.add(user)
        db.commit()
        db.close()
        
        return jsonify({"message": "Usuário criado com sucesso"}), 201
        
    except Exception as e:
        print(f"Erro no registro: {e}")
        return jsonify({"error": "Erro ao criar usuário"}), 500

# ================= LOGIN =================

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        db = SessionLocal()
        
        user = db.query(User).filter_by(username=data["username"]).first()
        db.close()
        
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 401
        
        if check_password_hash(user.password, data["password"]):
            token = jwt.encode({
                "user": user.username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }, SECRET_KEY, algorithm="HS256")
            
            return jsonify({
                "token": token,
                "user": user.username,
                "message": "Login realizado com sucesso"
            })
        else:
            return jsonify({"error": "Senha incorreta"}), 401
            
    except Exception as e:
        print(f"Erro no login: {e}")
        return jsonify({"error": "Erro ao processar login"}), 500

# ================= PROFILE =================

@app.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    return jsonify({"user": current_user})

# ================= PRODUCTS =================

@app.route("/products", methods=["GET"])
def get_products():
    try:
        db = SessionLocal()
        products = db.query(Product).all()
        
        result = []
        for p in products:
            result.append({
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "oldPrice": p.old_price,
                "rating": p.rating,
                "freeShipping": p.free_shipping,
                "category": p.category,
                "image": p.image
            })
        
        db.close()
        return jsonify(result)
    except Exception as e:
        print(f"Erro ao buscar produtos: {e}")
        return jsonify([])

# ================= ADMIN: ADICIONAR PRODUTO =================

@app.route("/admin/products", methods=["POST"])
@token_required
def add_product(current_user):
    if current_user != "admin":
        return jsonify({"error": "Acesso negado. Apenas administradores."}), 403
    
    try:
        data = request.json
        db = SessionLocal()
        
        new_product = Product(
            name=data["name"],
            price=data["price"],
            old_price=data.get("old_price", 0),
            rating=data.get("rating", 4.5),
            free_shipping=data.get("free_shipping", False),
            category=data["category"],
            image=data["image"]
        )
        
        db.add(new_product)
        db.commit()
        db.close()
        
        return jsonify({"message": "Produto adicionado com sucesso"}), 201
        
    except Exception as e:
        print(f"Erro ao adicionar produto: {e}")
        return jsonify({"error": "Erro ao adicionar produto"}), 500

# ================= ADMIN: DELETAR PRODUTO =================

@app.route("/admin/products/<int:product_id>", methods=["DELETE"])
@token_required
def delete_product(current_user, product_id):
    if current_user != "admin":
        return jsonify({"error": "Acesso negado. Apenas administradores."}), 403
    
    try:
        db = SessionLocal()
        product = db.query(Product).filter_by(id=product_id).first()
        
        if not product:
            db.close()
            return jsonify({"error": "Produto não encontrado"}), 404
        
        db.delete(product)
        db.commit()
        db.close()
        
        return jsonify({"message": "Produto excluído com sucesso"}), 200
        
    except Exception as e:
        print(f"Erro ao deletar produto: {e}")
        return jsonify({"error": "Erro ao deletar produto"}), 500

# ================= REGISTRAR PEDIDO =================

@app.route("/orders", methods=["POST"])
@token_required
def create_order(current_user):
    try:
        data = request.json
        db = SessionLocal()
        
        # Buscar user_id
        user = db.query(User).filter_by(username=current_user).first()
        user_id = user.id if user else None
        
        order = Order(
            user_id=user_id,
            username=current_user,
            items=data.get("items", []),
            total=data["total"],
            payment_method=data["payment_method"],
            customer_data=data.get("customer_data", {})
        )
        
        db.add(order)
        db.commit()
        db.close()
        
        return jsonify({"message": "Pedido registrado com sucesso"}), 201
        
    except Exception as e:
        print(f"Erro ao registrar pedido: {e}")
        return jsonify({"error": f"Erro ao registrar pedido: {str(e)}"}), 500

# ================= ANALYTICS (APENAS ADMIN) =================

@app.route("/admin/analytics", methods=["GET"])
@token_required
def get_analytics(current_user):
    if current_user != "admin":
        return jsonify({"error": "Acesso negado. Apenas administradores."}), 403
    
    try:
        db = SessionLocal()
        
        # Produtos
        products = db.query(Product).all()
        products_list = [{
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "category": p.category,
            "rating": p.rating,
            "free_shipping": p.free_shipping
        } for p in products]
        
        # Usuários
        users = db.query(User).all()
        users_list = [{
            "id": u.id,
            "username": u.username,
            "created_at": u.created_at.isoformat() if u.created_at else None
        } for u in users]
        
        # Pedidos
        orders = db.query(Order).all()
        orders_list = []
        for o in orders:
            items_count = sum([item.get("quantity", 1) for item in o.items]) if o.items else 0
            orders_list.append({
                "id": o.id,
                "username": o.username,
                "order_date": o.order_date.isoformat(),
                "total": o.total,
                "payment_method": o.payment_method,
                "items_count": items_count
            })
        
        # Estatísticas
        total_products = len(products_list)
        total_users = len(users_list)
        total_orders = len(orders_list)
        total_revenue = sum([o["total"] for o in orders_list])
        
        db.close()
        
        return jsonify({
            "products": products_list,
            "users": users_list,
            "orders": orders_list,
            "total_products": total_products,
            "total_users": total_users,
            "total_orders": total_orders,
            "total_revenue": total_revenue
        })
        
    except Exception as e:
        print(f"Erro ao buscar analytics: {e}")
        return jsonify({"error": f"Erro ao buscar dados: {str(e)}"}), 500

# ================= REDEFINIR SENHA =================

@app.route("/reset-password", methods=["POST"])
def reset_password():
    try:
        data = request.json
        db = SessionLocal()
        
        user = db.query(User).filter_by(username=data["username"]).first()
        if not user:
            db.close()
            return jsonify({"error": "Usuário não encontrado"}), 404
        
        # Atualizar senha
        user.password = generate_password_hash(data["new_password"])
        db.commit()
        db.close()
        
        return jsonify({"message": "Senha redefinida com sucesso"}), 200
        
    except Exception as e:
        print(f"Erro ao redefinir senha: {e}")
        return jsonify({"error": "Erro ao redefinir senha"}), 500


# ================= RUN =================

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)