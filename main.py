from flask import Flask, render_template, request, redirect
import sqlalchemy
from sqlalchemy.schema import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
engine = sqlalchemy.create_engine('sqlite:///fake.db', echo=True)

Base = declarative_base()


class Contato(Base):
    __tablename__ = 'contatos'  # campo obrigatório
    id = Column(Integer, primary_key=True)  # campo obrigatório
    nome = Column(String(100))
    email = Column(String(100))
    celular = Column(String(100))
    tags = Column(String(100))
    links = Column(String(100))


Base.metadata.create_all(engine)

# criar contato


def criar_contato_sql(contato: Contato):
    Session = sessionmaker(bind=engine)
    session = Session()
    # criando a sessão
    session.add(contato)
    session.commit()
    return 'sucess'

# deletar contato


def deletar_contato_sql(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    contato_del = session.query(Contato).filter_by(id=id).first()
    session.delete(contato_del)
    session.commit()
    return 'sucess'

# buscar contato


def buscar_contato_sql():
    Session = sessionmaker(bind=engine)
    session = Session()
    contatos = session.query(Contato).all()
    return contatos


app = Flask(__name__)


@app.route("/")
def index():
    contatos_ = buscar_contato_sql()
    return render_template("index.html", contatos=contatos_, id=id, zip=zip)


@app.route("/salvar_contato", methods=['POST'])
def salvar_contato():
    cont = Contato(nome=request.form['nome'],
                   email=request.form['email'],
                   celular=request.form['celular'],
                   tags=request.form['tags'],
                   links='familia')
    criar_contato_sql(cont)
    return redirect('/')


@app.route("/deletar_contato", methods=['POST'])
def deletar_contato():
    deletar_contato_sql(request.form['id'])
    return redirect('/')


app.run(debug=True)
