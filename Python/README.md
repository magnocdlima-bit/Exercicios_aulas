# Exercícios Python

## API de alunos

No PowerShell, na raiz do repositório:

```powershell
cd Python/api-alunos
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install Flask
python api.py
```

Rotas disponíveis: `/`, `GET /alunos`, `GET /alunos/<id>` e `POST /alunos`.

## App com template

Pare o servidor anterior e, em um novo terminal PowerShell na raiz do repositório, crie outro ambiente virtual:

```powershell
cd Python/app-flask
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install Flask
python main.py
```

O template da página inicial está em `app-flask/templates/index.html`.

Os ambientes `.venv/` são locais e estão excluídos do Git.