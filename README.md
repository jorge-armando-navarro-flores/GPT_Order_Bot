---
title: GPT Order Bot
emoji: 🔥
colorFrom: red
colorTo: gray
sdk: gradio
sdk_version: 4.39.0
app_file: app.py
pinned: false
license: cc
---

# Simple Order-Taking Chatbot

## Description

This is a simple chatbot that allows users to place orders through a chat interface built with Gradio and Python, leveraging the OpenAI library for natural language processing. Users can choose between several kinds of stores and different GPT models. Once the order is placed, the chatbot sends a confirmation and the details of the order to the user's email. This project is designed to be easy to deploy and use, making it suitable for small businesses or personal projects.

## Features

- Takes orders through a Gradio-based chat interface
- Users can choose between different kinds of stores
- Offers a selection of GPT models for natural language processing
- Sends order confirmation and details to the user's email
- Simple and user-friendly interface

## Technologies Used

- **Python**: Programming language
- **Gradio**: For creating the chat interface
- **OpenAI**: For natural language processing
- **SMTP**: For sending email messages

## Setup and Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/jorge-armando-navarro-flores/GPT_order_bot.git

   cd GPT_order_bot
   ```

2. **Create a Virtual Environment**

   ```sh
   python -m venv venv

   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add your email and OpenAI credentials:

   ```env
   SMTP_SERVER=your_smtp_server
   SMTP_PORT=4your_smtp_port
   EMAIL_ADDRESS=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   ```

5. **Run the Chatbot**

   ```sh
   python app.py
   ```

## Usage

1. **Start the Chatbot**

   Run the `app.py` script to start the Gradio interface. Navigate to the URL provided by Gradio (e.g., `http://localhost:7860`) to start interacting with the chatbot.

2. **Choose a Store and GPT Model**

   Select the type of store you want to order from and the GPT model you want to use for processing your order.

3. **Place an Order**

   Follow the chatbot prompts to place your order. The chatbot will ask for details such as item name, quantity, and any special instructions.

4. **Receive Order Confirmation**

   Once the order is placed, the chatbot will send a confirmation email with all the order details to the email address you provided.

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request

## License

This project is licensed under the CC License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or issues, please open an issue in the repository or contact me at [jorge.armando.navarro.flores@gmail.com](mailto:jorge.armando.navarro.flores@gmail.com).

---
