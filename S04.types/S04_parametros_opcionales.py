def say_hi(name: str | None = None):
      if name is not None:
        print(f"Hey {name}!")

      else:
        print("Hello world")
say_hi()     
say_hi("Mike lora")        
