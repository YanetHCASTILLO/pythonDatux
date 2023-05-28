#texto
import re
texto = "La fiesta fue en la casa de mi amiga"
textoencontrado=re.search('la', texto)
print(textoencontrado)

#numero
def validtNumber(numero):
    patron=r'^9\d*$'
    a=re.match(patron,numero)
    print(a)
    
validtNumber('97895')

#correo
body_regex = re.compile('''
    ^(?!\.)                           
    (
      [-a-z0-9!\#$%&'*+/=?^_`{|}~]     
      |
      (?<!\.)\.                        
    )+
    (?<!\.)$                            
''', re.VERBOSE | re.IGNORECASE)
domain_regex = re.compile('''
    (
      localhost
      |
      (
        [a-z0-9]
           
        (
          [-\w]*                         
          [a-z0-9]                       
        )?
      \.                               
      )+
      [a-z]{2,}                        
   )$
''', re.VERBOSE | re.IGNORECASE)

def is_valid_email(email):
    if not isinstance(email, str) or not email or '@' not in email:
        return False
    
    body, domain = email.rsplit('@', 1)

    match_body = body_regex.match(body)
    match_domain = domain_regex.match(domain)

    if not match_domain:
        try:
            domain_encoded = domain.encode('idna').decode('ascii')
        except UnicodeError:
            return False
        match_domain = domain_regex.match(domain_encoded)

    return (match_body is not None) and (match_domain is not None)

print(is_valid_email('net@gmail.com')) 
print(is_valid_email('anast@gmail.com')) 
print(is_valid_email('abc@edu.pe')) 

#celular
regex = r"^(\(?\+[\d]{1,3}\)?)\s?([\d]{1,5})\s?([\d][\s\.-|.]?){6,7}$"
result = re.match(regex, "+51 996 234 675")
print(result)