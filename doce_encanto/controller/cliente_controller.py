from flask import Blueprint, request, jsonify
from model.cliente import Cliente, db

cliente_bp = Blueprint('cliente', __name__)

# Método CRUD - Criação (Create)
@cliente_bp.route('/', methods=['POST'])
def criar_cliente():
    dados = request.json
    novo_cliente = Cliente(
        nome=dados['nome'],
        email=dados['email'],
        whats=dados.get('whats', '')
    )
    db.session.add(novo_cliente) # Adiciona o cliente à sessão
    db.session.commit() # Salva a sessão no banco de dados
    return jsonify(novo_cliente.to_dict()), 201

# Método CRUD - Leitura (Find All)
@cliente_bp.route('/', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all() # Recupera todos os clientes da tabela
    return jsonify([cliente.to_dict() for cliente in clientes])

# Método CRUD - Leitura por ID (Find by ID)
@cliente_bp.route('/<int:id>', methods=['GET'])
def obter_cliente(id):
    cliente = Cliente.query.get(id) # Busca o cliente pelo ID
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    return jsonify(cliente.to_dict())

# Método CRUD - Leitura por Nome (Find by Name)
@cliente_bp.route('/busca', methods=['GET'])
def buscar_por_nome():
    nome = request.args.get('nome')
    if not nome:
        return jsonify({'erro': 'Parâmetro "nome" é obrigatório'}), 400
    clientes = Cliente.query.filter(Cliente.nome.like(f'%{nome}%')).all()
    return jsonify([cliente.to_dict() for cliente in clientes])

# Método CRUD - Atualização (Update)
@cliente_bp.route('/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    cliente = Cliente.query.get(id) # Recupera o cliente pelo ID
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    dados = request.json
    cliente.nome = dados.get('nome', cliente.nome) # Atualiza os dados
    cliente.email = dados.get('email', cliente.email)
    cliente.whats = dados.get('whats', cliente.whats)
    db.session.commit() # Persiste as alterações no banco
    return jsonify(cliente.to_dict())

# Método CRUD - Exclusão (Delete)
@cliente_bp.route('/<int:id>', methods=['DELETE'])
def excluir_cliente(id):
    cliente = Cliente.query.get(id) # Recupera o cliente pelo ID
    if not cliente:
        return jsonify({'erro': 'Cliente não encontrado'}), 404
    db.session.delete(cliente) # Marca o cliente para exclusão
    db.session.commit() 
    return jsonify({'mensagem': 'Cliente excluído'}), 200

# Contagem - Número total de registros
@cliente_bp.route('/total', methods=['GET'])
def contar_clientes():
    total = Cliente.query.count()
    return jsonify({'total_clientes': total})