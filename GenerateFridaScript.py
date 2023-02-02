def extract_until_char(s, c):
  index = s.find(c)
  if index == -1:
    return s
  else:
    return s[:index]
    
def getAddress(doc):
    adr = hex(doc.getCurrentAddress())
    string = "".join(adr)
    inverted = string[::-1]
    return "0x"+extract_until_char(inverted,"0")[::-1]

doc = Document.getCurrentDocument()
script = "var targetModule= '" + doc.getExecutableFilePath().split('/')[-1]+"'"
address = getAddress(doc)
script += """
var addr=ptr(%s);
var moduleBase=Module.getBaseAddress(targetModule);
var targetAddress=moduleBase.add(addr);
Interceptor.attach(targetAddress,{
    onEnter:function(args){
        console.log("onEnter")
    },
    onLeave(retval){
        console.log("onLeave")
    }
});
""" %  address
 
print(script)

