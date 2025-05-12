from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
 
# Load model and tokenizer
model_dir = "/Users/I528928/convertedhfmodel"  # Path to your converted model
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForCausalLM.from_pretrained(model_dir)
 
# Move to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
 
# Interactive prompt loop
while True:
    # Get user input
    user_input = input("Enter your prompt (or 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
    # Format prompt for Llama 3.2 Instruct
    prompt = f"[INST] {user_input} [/INST]"
    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    # Generate response
    outputs = model.generate(
        **inputs,
        max_length=100,           # Adjust for desired response length
        do_sample=True,           # Enable sampling for varied responses
        top_p=0.9,                # Nucleus sampling
        temperature=0.7,          # Control randomness
        pad_token_id=tokenizer.eos_token_id  # Handle padding
    )
    # Decode and print response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\nResponse:", response, "\n")