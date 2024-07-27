import os
import gradio as gr
from completion_tools import OpenAITools
from contexts import store_types, pizza_shop_context
from email_sender import send_email
from dotenv import load_dotenv

load_dotenv()

tools = OpenAITools()
interac = bool(int(os.environ.get("INTERACTIVE")))

with gr.Blocks() as demo:
    appTitle = gr.Label("GPT Order Bot", color="#6EACDA")
    with gr.Row():
        with gr.Column(scale=1):   
            apikey = gr.Textbox(label="Open AI API key", placeholder="Input your OpenAI API key", type="password")
            model = gr.Dropdown(label="Model", value="gpt-3.5-turbo", choices=["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4o"])
            context = gr.Dropdown(label="Store type", value=store_types[0], choices=store_types)
            label = gr.Label("Set your Order Bot")
            gr.Markdown("If you want to send confirmation email you must run it locally [GitHub repo](https://github.com/jorge-armando-navarro-flores/GPT_order_bot)")
            email = gr.Textbox(label="Email", placeholder="Input your Email", interactive=interac)
            print(type(interac))
            send = gr.Button("Send Confirmation Email", interactive=interac)
            
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(pizza_shop_context, type="messages")
            msg = gr.Textbox()
            clear = gr.ClearButton([msg, chatbot])

            def respond(message, chat_history):
                try:
                    chat_history.append({'role':'user', 'content': message})
                    bot_message = tools.get_completion_from_messages(chat_history) if chat_history else tools.get_completion(message) 
                    chat_history.append({'role':'assistant', 'content':bot_message})
                    return "", chat_history, "Your order bot is working"
                except:
                    return "", pizza_shop_context, "There is somenthing wrong with your Open AI API key"
            
    apikey.input(tools.set_api_key, inputs=[apikey])
    model.input(tools.set_model, inputs=[model])
    context.input(tools.set_context, inputs=[context], outputs=[chatbot, msg, label])
    msg.submit(respond, [msg, chatbot], [msg, chatbot, label])
    send.click(send_email, inputs=[chatbot, email, apikey], outputs=[label])

demo.launch(share=True)
