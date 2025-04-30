import azure.functions as func
import logging

app = func.FunctionApp()


def double_consonants(text: str) -> str:
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char.isalpha() and char not in vowels:
            result += char * 2
        else:
            result += char
    return result


@app.route(route="DoubleConsonants", auth_level="anonymous")
def run(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing DoubleConsonants function.")

    try:
        data = req.get_json()
        input_text = data.get("text", "")
        result = double_consonants(input_text)
        return func.HttpResponse(result, status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=400)
