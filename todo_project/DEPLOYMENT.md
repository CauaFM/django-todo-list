# Deploy no Google Cloud

Este guia resume como publicar o projeto diretamente a partir do GitHub utilizando Cloud Run (recomendado para apps Django containerizados). Os passos assumem que você já possui o `gcloud` instalado e autenticado.

## 1. Preparar o repositório

1. Crie um fork ou repositório no GitHub e envie o conteúdo desta pasta (`todo_project`).
2. Defina os segredos/variáveis de ambiente que serão usados em produção (exemplo em `env.sample`). Os principais:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=seu-dominio.com`
   - `DJANGO_CSRF_TRUSTED_ORIGINS=https://seu-dominio.com`
   - `DATABASE_URL` (por exemplo, conexão do Cloud SQL)

## 2. Configurar build no Google Cloud

1. Crie um repositório no Artifact Registry (ex.: `gcp-project-region-docker.pkg.dev/PROJECT_ID/todo`).
2. Configure o Cloud Build Gatilho (Trigger) apontando para o seu repositório GitHub. Use:
   - **Tipo de build**: Dockerfile
   - **Diretório**: `todo_project`
   - **Dockerfile**: `todo_project/Dockerfile`
3. O build produzirá uma imagem que poderá ser usada pelo Cloud Run.

## 3. Implantar no Cloud Run

Depois de uma imagem estar no Artifact Registry (via trigger ou `gcloud builds submit`), execute:

```bash
gcloud run deploy todo-web \
  --image=gcp-project-region-docker.pkg.dev/PROJECT_ID/todo/IMAGE:TAG \
  --region=REGION \
  --allow-unauthenticated \
  --set-env-vars DJANGO_SECRET_KEY=...,DJANGO_DEBUG=False,DJANGO_ALLOWED_HOSTS=sua-url,DJANGO_CSRF_TRUSTED_ORIGINS=https://sua-url,DATABASE_URL=...
```

> Se utilizar Cloud SQL, adicione `--add-cloudsql-instances` e inclua o conector Unix na `DATABASE_URL`.

## 4. Migrações e dados

Após o deploy, rode as migrações executando um job temporário no Cloud Run ou Cloud Build:

```bash
gcloud run jobs create todo-migrate \
  --image gcp-project-region-docker.pkg.dev/PROJECT_ID/todo/IMAGE:TAG \
  --region REGION \
  --command "python" \
  --args "manage.py","migrate"
```

Execute o job:

```bash
gcloud run jobs execute todo-migrate --region REGION
```

## 5. Coleta de estáticos

O Dockerfile já executa `collectstatic` durante o build. Caso altere assets e prefira coletar via job, rode:

```bash
python manage.py collectstatic --noinput
```

## Observações

- O arquivo `requirements.txt` define as dependências necessárias para buildar a imagem.
- O `STATIC_ROOT` é `staticfiles/` e é servido via WhiteNoise, adequado para Cloud Run.
- Ajuste regras de firewall/domínio (Cloud Run custom domain) conforme necessidade.


