# AskSQL AI

AskSQL AI is an intelligent SQL builder app that leverages AI to generate SQL queries based on user-provided database schemas and questions. Built with LangChain and Streamlit, this tool simplifies query creation, making it perfect for data analysts, developers, and anyone working with databases.

## Features

- **Schema Memory**: Remembers your provided database schema until a new one is set.
- **Dynamic SQL Generation**: Generates precise SQL queries based on your questions and schema.
- **Fallback Responses**: If a question isn't related to the schema, the app attempts to answer and suggests providing a schema for accurate SQL.
- **Interactive UI**: Built with Streamlit for a smooth and intuitive user experience.

## Demo

![AskSQL AI Demo](demo.gif)  <!-- Add a demo gif or screenshot here -->

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/arghads9177/asksql-ai.git
cd asksql-ai
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**

```bash
streamlit run app.py
```

## Usage

1. **Provide a Database Schema:**
   - Go to the sidebar and paste your database schema.
   - Click **Set Schema** to save it.

2. **Ask Questions:**
   - Enter your SQL-related question in the main input box.
   - Click **Generate SQL** to get the SQL query based on your schema.

3. **Update Schema:**
   - Provide a new schema in the sidebar to overwrite the existing one.

4. **Unrelated Questions:**
   - If your question isn't related to the schema, AskSQL AI will still attempt to answer and prompt you to provide a schema for better accuracy.

## Example

**Schema:**
```sql
Tables:
1. Customers (CustomerID, Name, Age, City)
2. Orders (OrderID, CustomerID, ProductID, Quantity, OrderDate)
3. Products (ProductID, ProductName, Price)
```

**Question:**
```
List all customers who have placed an order in January 2024.
```

**Generated SQL:**
```sql
SELECT Customers.Name, Customers.City 
FROM Customers 
JOIN Orders ON Customers.CustomerID = Orders.CustomerID 
WHERE Orders.OrderDate BETWEEN '2024-01-01' AND '2024-01-31';
```

## Technologies Used

- [LangChain](https://www.langchain.com/) – For AI-driven language processing.
- [Streamlit](https://streamlit.io/) – For building an interactive web application.
- [OpenAI GPT](https://openai.com/api/) – For natural language understanding and SQL generation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Created by [Argha Dey Sarkar](https://github.com/arghads9177). Feel free to reach out!

---

*Empower your data queries with AskSQL AI!*

