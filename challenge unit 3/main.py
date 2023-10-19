def linearSearchproduct(productlist,targetproduct):
  indices=[]

  for index,product in enumerate(productlist):
   if product==targetproduct:
    indices.append(index)

  return indices

#Example usage:
products=["shoes","boo","loafer","shoes","sandel","shoes"]
target="shoes"
target2='apple'

result=linearSearchproduct(products,target2)
print(result)



  