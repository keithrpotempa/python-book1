
# --------------- DECORATORS --------------- 
def whodunnit(func, by_whom):
    def new_sentence(*args, **kwargs):
      original_sentence = func()
      return f"{original_sentence} {by_whom}"
    return new_sentence

def kids(func):
    return whodunnit(func, "by the kids")
  
def dad(func):
    return whodunnit(func, "by Dad")
  
def mom(func):
    return whodunnit(func, "by Mom")
    
    
# --------------- FUNCTIONS ---------------     
@dad
def laundry():
    return "The dirty laundry was cleaned"

@mom
def garbage():
    return "The garbage was taken out"

@dad
def dust():
    return "The house was dusted"

@kids
def groom():
    return "The dog was brushed"

# --------------- CALLS ---------------       
print(laundry())
print(garbage())
print(dust())
print(groom())