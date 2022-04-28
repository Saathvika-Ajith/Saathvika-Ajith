{% include navigation.html %}

### [Create Task Runtime](http://127.0.0.1:5000/)

Task Overview:
* Final code: Needs to be a pdf, and must include comments
* One video section: Not much explanation necessary, Purpose and function of code, No talking
* 4 written code: Data abstraction, Managing complexity, Procedural abstraction, Algorithm implementation

Written Responses:
* 15 questions about the function in code, and the video that you made
* All related to the create task project, 4 parts: Describe program, functionality, and input/output (3 qs), Show understanding of list/collection types (5 qs), Show self-made developed procedure, must include sequencing, selection, iteration, and things learned (4qs), Explanation of self-developed procedure (6 qs) **Note: 750 word limit for each section should take 50-100 words**

Ideas:
* Solves problem
* Enables innovation
* Express creativity
* Explore personal interests
* Complex games
* Past projects: Job finder, Music editor

Data Abstraction: 
* Data Abstraction is the reduction of a particular body of data to a simplified representation of the whole. It essentially allows the programmer to reduce the amount of code they have to write by simplifying the entirety of it. Data Abstraction usually hides details of a program in order to make it easier to develop and maintain a program.
* [Example of Data Abstraction](https://github.com/samayass/flask_portfolio/commit/b3366dbb9d8228090746ac992f8b7d90695f255b#:~:text=let%20time%20%3D%20new,sec%20%3D%20time.getSeconds()%3B)
* In our quiz, we will most likely use data abstraction to set up the point system for each option (A, B, C, D, etc) for the questions in order to simplify how we will score the quizzes. 

Procedural Abstraction
* Procedural Abstraction allows procedure to be used without needing to know the details of how it works (the name tells you what the procedure does)
* We will most likely to make a procedure/function that calculate the total points that the user get from the answer choices, and we can name this procedure as "calculate_total" and we can call the procedure by the name which also helps manage the complexity and reduce redundancy in code.

Managing complexity
* The code will be strictly organized.
* All javascript functions will be in a specific .js file and the code within will be organized and called multiple times.
* The Html will be neatly designed and formatted, as will the main.py.
* Each procedure that is run in the code will be coded completely separate and not tangled up in other processes.

Algorithm implementation
* There will be an algorithm that tallies up the users’ answers to the quiz and determines which god their personality is the most like.
* A numerical value will be assigned to each of the options, and different ranges of ending point values will correspond to different Greek gods.
* Either a python or javascript function.



## Written Response Questions - BLACKPINK Quiz
- Questions | Answers 

- 3ai - Describes the overall purpose of the program  | Our interactive quizes are fun personality quizzes to pass the time, entertain, and help people learn more about themselves. There are two quizzes, the first being "Which Blackpink Member Are You?" and the second, "Which Greek Goddess Are You?". Each quiz has an algorithm which tallies the point values from each option that you pick, and presents your score as which person's personality, your personality is the most like, according to the insights derived from your responses.

- 3aii - Describes what functionality of the program is demonstrated in the video | The video demonstrates a user taking both the quizzes from top to bottom. In it, the user clicks and interacts with the multiple header background buttons on the very top of the program, and then takes the two quizzes, each containing 4 questions with 4 different options that the user can click on. A numerical value (1, 2, 3 or 4) is assigned to each of the options, and different ranges of ending point values will correspond to different Blackpink members/Greek Goddesses. After the user is done answering all of the questions, the quiz contains a submit button which the user  clicks on and the program calculates the total score that the user got and displays the name and picture of the corresponding person. Below that but only in the Blackpink quiz, there is a random Blackpink fact generator API that we created ourselves.

- 3aiii - Describes the input and output of the program demonstrated in the video  | In the video, the inputs are all the options that the user choses while answering the questions. Then, the output is the name and picture of the person that the user's personality is the most like based on the user's choices. It will be displayed onscreen only after answering all the questions and clicking the submit button.


- 3bi - The first program code segment must show how data have been stored in the list.  |![factlist](https://user-images.githubusercontent.com/89208817/165831038-0ea7885d-e210-4413-9c00-33f37a03ddeb.png)


- 3bii - The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose.  | ![factfront](https://user-images.githubusercontent.com/89208817/165833697-a7a4ce55-cc08-420f-b6ef-f9f259ae815c.png)<br>![factback](https://user-images.githubusercontent.com/89208817/165833709-e267c658-3b1e-43fb-b83e-b8198ad3a22d.png)

- 3biii - Identifies the name of the list being used in this response  | The list used in the code above is named "facts".  

- 3biv - Describes what the data contained in the list represent in your program | The data contained in the list are strings of a few interesting and fun facts about the successful K-pop girl-group and international sensation Blackpink.

- 3bv - Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list   |  The list allows for the program to store all the facts in one location. Without it holding the all facts the program would become redundant, plus the length of the facts are pretty long. You would have to resort to using different variables to hold many different facts, causing the API to be inefficient and the code to be messy and convuluted. 

- 3ci - The first program code segment must be a student-developed procedure that:□ Defines the procedure’s name and return type (if necessary) □ Contains and uses one or more parameters that have an effect on the functionality of the procedure □ Implements an algorithm that includes sequencing, selection, and iteration  | ![mainfunction](https://user-images.githubusercontent.com/89208817/165835717-3bdd7785-d885-428a-ab97-5ebe5b7c9463.png)

- 3cii - The second program code segment must show where your student-developed procedure is being called in your program.  | ![display](https://user-images.githubusercontent.com/89208817/165836205-1402f295-d071-40ba-b151-d8fdc9e853f8.png)

- 3ciii - Describes in general what the identified procedure does and how it contributes to the overall functionality of the program  | This function makes it so that if your answer choices (which have certain points depending on which answer option is chosen) add up to be in a particular range, you will receive the specific person allocated to that point range. The nested Boolean statements are used to systematically determine where the user's score falls.

- 3civ - Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.  | First, the point values for each question the user answered are stored and totaled as "result". Second, this numerical value is sent through a set of nested Boolean statements which determine which range of numbers the final point value is between, with there being 4 different ranges corresponding to 4 different Greek Goddesses. The algorithm keeps going until "result" falls within a certain range, and that goddesses is selected as the best personality match. This is saved as "result2" and it's what displays when the user clicks submit.

- 3di - Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute.  | The first call is when the submit function calls the function to total up the point values of the answers the user chose and and save them as "result". The second call is when below the submit button "result2" is called from the function and the goddess that matches the user's personality the most is displayed.

- 3dii - Describes what condition(s) is being tested by each call to the procedure  | During the first call, the condition that must be met are that all the questions need to be answered, and the submit button pushed. For the second call, the condition that needs to be met is that the point value of the user's result must be between 4 and 16, which it always is if the quiz is taken properly.

- 3diii - Identifies the result of each call | The final result is the point values for all of the user's answers being tallied up, matched to a person with that point value range, and their picture being displayed as the result of the quiz so the user knows who their personality is the most like, concluding a truly thrilling speedrun of self-discovery.
