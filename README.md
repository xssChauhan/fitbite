# fitbite
Initial Release for APIs for fitbite backend.

1st Use Case: Getting Products
  * **/api/[auth token]/get/products** :  Returns a JSON object containing the list of all the products. Each list contains following information:
    * Product ID
    * Product Name
    * Locations for images of the product
    * Price of the product
  * **/api/[auth token]/get/product/[product id** : Returns a JSON object containing the list of all the products. Each product has the following information:
    * Product ID
    * Product Name
    * Images of the product
    * Price
    * Description
    * Other meta information like tags, categories, etc
  * **/api/[auth token]/get/productImage/[filename]** :  Returns images as an HTTP response. Please use the filenames obtained in the products APIs for making this request.
