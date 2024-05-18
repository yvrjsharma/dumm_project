import gradio as gr
import time
import random 

with gr.Blocks() as demo:
	with gr.Row():
		in = gr.Textbox(label='name')
		out = gr.Textbox(label='greet')
	bn = gr.Button()
	bn.click(lambda x: "hello, " + str(x), in, out )

demo.launch()
	
