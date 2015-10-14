# fitbite
Initial Release for APIs for fitbite backend.


  * **/api/get/products** :  Returns a JSON object containing the list of all the products. Each list contains following information:
    * Product ID
    * Product Name
    * Locations for images of the product
    * Price of the product
  * **/api/get/product/[product id]** : Returns a JSON object containing the list of all the products. Each product has the following information:
    * Product ID
    * Product Name
    * Images of the product
    * Price
    * Description
    * Other meta information like tags, categories, etc
  * **/api/get/productImage/[filename]** :  Returns images as an HTTP response. Please use the filenames obtained in the products APIs for making this request.
  * **/api/startSession/[app_id]** : Registers a session with the server and returns in response the session key. This key is used to authenticate further API calls.
  * **/api/endSession/[session_key]** : Call the API to delete the session from the serveer.


Session management shall change with the ability to uniquely identify each app with a key. Right now it is possible for an app to register multiple sessions. With the introduction of key/SessionID pair, each app would be able to register one session only.
