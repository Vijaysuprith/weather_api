# Weather_API with flask 
This projects allows the users to retrieve the information which contains the current weather information for multiple locations, this data is taken with the help of generated API key which was generated using OpenWeatherMap API.

##Prerequisites
* python
* flask
* request packages
* postman for testing API endpoints
* API key generated from OpenWeatherMap API

## Brief Procedure
1. Install the required libraries.
2. To run the program we need to generate the API key using the OpenWeatherMap APi key.
3. Run the application , once the code is compiled , open the Postman and create a new request to  `http://127.0.0.1:5000/weather` with the `GET` method.
4. Add a query parameter 'city' with the value being the city.
5. For example (city=Mysore).
6. Once its done , send the request and get the output.To check the accuracy of the Output which contains the weather data by `OpenWeatherMap`.

##Detailed explanation
1. Run the Python script using the virtual environment by using idle or VScode.
2. The script contains the base url `http://127.0.0.1:5000`. When you click on this url, you will see 404 error.
3. Now by creating the new Workspace in the Postman worksapce, set the request type to 'GET'.
4. In the URL column enter Enter the URL for your Flask API endpoint i.e, `http://127.0.0.1:5000/weather?`.
5.  Click on the "Params" tab. In the "Key" column, enter `location`. In the "Value" column, enter the city for which you want to retrieve the weather information.
6.  click the send button the data will be retrieved in the form of JSON file.


##screenshots
