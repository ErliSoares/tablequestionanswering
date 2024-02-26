## API para responder perguntas sobre informações contidas em uma tabela

Todos créditos para: https://huggingface.co/spaces/patrawtf/shopify_csv_qa

Para rodar o projeto: `docker-compose up`.

As requisições podem serem enviadas para `POST http://localhost:5000/ai/question`, o arquivo `request_example.json`
tem um exemplo do corpo da requisição com mais dados, abaixo um exemplo simplificado:

```JAVASCRIPT
POST http://localhost:5000/ai/question
Content-Type: application/json

{
    "question": "What is the highest order_amount?",
    "data": [
        {
            "shop_id": 53,
            "user_id": 746,
            "order_amount": 224,
            "total_items": 2,
            "payment_method": "cash",
            "created_at": "2017-03-13 12:36"
        },
        {
            "shop_id": 92,
            "user_id": 925,
            "order_amount": 90,
            "total_items": 1,
            "payment_method": "cash",
            "created_at": "2017-03-03 17:38"
        }
    ]
}

### response: 224
```