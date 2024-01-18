import paralleldots
# Setting your API key
def kompner(text):
      paralleldots.set_api_key('nvL4UbtjIMLtusckrfOgkUDQQcXaPsgnae2X5QXeHs4')
      # Get your API key here
      # Viewing your API key
      paralleldots.get_api_key()
      # Examples
      ner = paralleldots.ner(text) 
      return ner