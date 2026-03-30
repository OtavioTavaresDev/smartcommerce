from database import engine, SessionLocal
from models import Product, Base, User, Order
from werkzeug.security import generate_password_hash
import os
from datetime import datetime

print("=== RECRIANDO BANCO DE DADOS ===\n")

# Deletar banco antigo
if os.path.exists("store.db"):
    os.remove("store.db")
    print("✓ Banco antigo removido")

# Criar tabelas
Base.metadata.create_all(bind=engine)
print("✓ Tabelas criadas\n")

db = SessionLocal()

# ================= CRIAR USUÁRIOS =================
print("Criando usuários:")

# Usuário admin
hashed_admin = generate_password_hash("1234")
admin = User(username="admin", password=hashed_admin, created_at=datetime.utcnow())
db.add(admin)
print(f"  ✓ admin / 1234")

# Usuário demo
hashed_demo = generate_password_hash("demo123")
demo = User(username="demo", password=hashed_demo, created_at=datetime.utcnow())
db.add(demo)
print(f"  ✓ demo / demo123")

db.commit()

# ================= CRIAR PRODUTOS =================
print("\nCriando produtos:")

products = [
    Product(name="Smartwatch Ultra X8", price=299.90, old_price=499.90, rating=4.8, free_shipping=True, category="eletronicos", image="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=300&fit=crop"),
    Product(name="Fones Bluetooth Pro ANC", price=189.90, old_price=299.90, rating=4.5, free_shipping=True, category="eletronicos", image="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&h=300&fit=crop"),
    Product(name="Camiseta Streetwear Oversized", price=79.90, old_price=129.90, rating=4.7, free_shipping=False, category="moda", image="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=300&fit=crop"),
    Product(name="Tênis Running Max Air", price=259.90, old_price=399.90, rating=4.9, free_shipping=True, category="moda", image="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400&h=300&fit=crop"),
    Product(name="Bola de Futebol Oficial", price=89.90, old_price=149.90, rating=4.6, free_shipping=False, category="esportes", image="https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=400&h=300&fit=crop"),
    Product(name="Raquete Tênis Profissional", price=199.90, old_price=299.90, rating=4.4, free_shipping=True, category="esportes", image="https://images.unsplash.com/photo-1554068865-24cecd4e34b8?w=400&h=300&fit=crop"),
    Product(name="Luminária Inteligente RGB", price=149.90, old_price=199.90, rating=4.7, free_shipping=False, category="casa", image="https://images.unsplash.com/photo-1565814329452-e1efa11c5b89?w=400&h=300&fit=crop"),
    Product(name="Kit Panelas Antiaderente", price=279.90, old_price=399.90, rating=4.8, free_shipping=True, category="casa", image="https://images.unsplash.com/photo-1584990347449-9a1e98f6d9a0?w=400&h=300&fit=crop"),
    Product(name="Câmera Action 4K", price=899.90, old_price=1299.90, rating=4.9, free_shipping=True, category="eletronicos", image="https://images.unsplash.com/photo-1605640840605-14ac1855827b?w=400&h=300&fit=crop"),
    Product(name="Jaqueta Jeans Premium", price=189.90, old_price=259.90, rating=4.5, free_shipping=False, category="moda", image="https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=300&fit=crop"),
]

for i, product in enumerate(products, 1):
    db.add(product)
    print(f"  ✓ {i}. {product.name}")

db.commit()
db.close()

print("\n" + "="*40)
print("✅ BANCO DE DADOS CRIADO COM SUCESSO!")
print("="*40)
print("\n📝 CREDENCIAIS PARA TESTE:")
print("   👤 admin    🔑 1234")
print("   👤 demo     🔑 demo123")
print("\n🚀 Agora execute: python app.py")