## Style.CSS


/* This file is used to add style onto your website */
body{
  background-color: #0f0019;;
}
h1 {
  color:#0f0019;;
  font-family:cursive;
  background-color: #edbd0c;
}

p {
  
 
}

p1  { 
  color: white;
}


p2 {
     
  padding-left: 5px;
  padding-right: 5px;
  color: white;
}

p3 { font-size: 24px;
    color: white;
    font-family:  fantasy;
    
  
}

h2{
   color:#226ddd;
  ;
  font-size: 20px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}

h3{
   color:#000000;

  font-style: oblique;
  text-decoration: underline;
  font-size: 20px;
  border: 3px solid black;
  background-color: #0f0019;;
  color: white;
  
}

h4{
   color:#226ddd;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 25px;

  
}

h5{
   color:#226ddd;
  font font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 30px;

  
}

h7 {
   color:#226ddd;
  ;
  font-size: 20px;

}

img{
  border-color: black;
  border-radius:
  align-items: center;

}


/* Centering pictures of  italy */





img {
  border: 5px solid #000000;
}


.bordered {
  padding-left: 10px;
  padding-right: 10px;
  border: 3px solid black;
  
}

.myParagraph {
  padding-left: 10px;
  padding-right: 10px;
  border: 3px solid black;
  color: white;
}


#myHeader{
 
   padding-left: 10px;
  padding-right: 10px;
  border: 3px solid black;
  background-color: #0f0019;;;
  color: white;
  
}

footer {
   padding-left: 10px;
  padding-right: 10px;
  font-size: 25px;
  background-color: #0f0019;;
  color: white;
  align-self: center;
}





.row {
  display: flex;
  flex-wrap: wrap;
  padding: 0 4px;
}

/* two columns for gallery */
.column {
  flex: 50%;
  padding: 0 4px;
}

.column img {
  margin-top: 8px;
  vertical-align: middle;
}


/* Contact info and form style  code */


/* Inputs */
input[type=text], select, textarea {
  width: 100%; 
  padding: 12px;  
 
  border: 1px solid #ccc; 
  border-radius: 4px; 
  box-sizing: border-box; 
  margin-top: 6px; 
  margin-bottom: 16px; 
  resize: vertical 
}

/* Submit button */
input[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* Color of submit button */
input[type=submit]:hover {
  background-color: #208325;
}

/* Colors and style for contact form */
.container {
  border-radius: 5px;
  background-color: #0f0019;
  padding: 20px;
}

h9 {
  color: white;
}





--------------------------------------------------
## INDEX.HTML
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>BrandonsPersonalWebsite.com</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  
  <script src="script.js"></script>

 
</body>
  <nav role="navigation"></nav>
    <main role="main">
        <header role="banner">
            <h1 id="myHeader"> Brandon Gonzalez</h1>
  <img src="lelouch!.jpeg" alt="Picture of my favorite anime main character" width="1885" height="325" </img>
          <br>
          <p3>  <br> Computer Scientist | Software  Engineer | Full Time Student 
          </p3>
         
            
        </header>

        <section>
          <h2>About me</h2>
          <br>

          <img src="me.jpeg" alt="Picture of myself! "  width="275" height="250" </img>

          <img src="princy.jpeg" alt="Picture of my dog named Princess." width="275" height="250" </img>
        

          <p class="myParagraph">Hello everyone! My name is Brandon Gonzalez and I am a first generation Florida International University hispanic Student, majoring in Computer Science seeking an internship and future career with a great company in order to perform productive and core programming, while learning how to implement hybrid roles into the day-to-day services that I will be a part of. Overall,  I am focused and wanting to excel in any company I am a part of,  wanting to make a positive impact in the community. I would love to be able to create technology and softwares so advanced, that it will change the world and bring benefits to anyone who uses it.
            <br>
          <br>
            Expected Graduation date: Summer of 2024.
          </p>  
        </section>

      <h5> Certifications / Skills </h5>
      <p2>-Certified in all Microsoft programs  (Word, powerpoint, Excel, etc.) <br>-Certified in Adobe programs such as photoshop, lightroom, after effects, and dreamweaver. <br> -Excelling in programming.</p2>
      
      
      <section>
        <h4>Fun facts</h4>
    <div> 
        <p1>-I compete in the sport of Powerlifting. <br>  -I like to go on daily walks to enjoy the nice weather of Florida.  <br> -I am into photography and videography, trying to get better at it day by day. <br> -Throughout highschool, I had dedicated over 100+ hours at the Zoo of Miami. <br>
          <br>
           Below this text, you'll find  some awesome pictures I took with my camera during my stay in Italy during the Winter.
<br>
          <br>

          <div class="row">
            
  <div class="column">
    <img src="italy1.png" alt="Picture of me 
 facing  a mountain range in Lake Como, Italy."  class="center"> 
    <img src="italy2.png" alt="Another picture of me facing  a mountain range in Lake Como, Italy." >
    <img src="italy3.png" alt="Sunset behind the beautiful mountains of Italy." >
    <img src="italy4.png" alt="Snowpeaked mountain tops with the view of the massive lake." >
  </div>
           
  
          
        <br></p1>
      </div>  
      </section>

     
      <br>
      

      <h2>Interview Video</h2>
        <section>
           
          <br>
          <div><iframe width="560" height="315" src="https://www.youtube.com/embed/-v7-PN9pKY4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
        </section>

<br>
      
      <h7> Collegiate State Championship Powerlifting Meet </h7>
      <br>
      <br>
      <div> <iframe width="560" height="315" src="https://www.youtube.com/embed/CcqBfyo9bH4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> </div>

      



      
      <h3>Contact Information
        <br>
      <img src="mail  clip art.jpg" alt="Picture of an envelope" width="120" height="120" </img>

        <img src="whatsapp.png"  alt="Picture of the whatsapp symbol for my contact info." width="120" height="120" </img>
    
        <section>

            Email: bgonz207@fiu.edu <br>
          Whatsapp: 305-803-6205
        </section>
         
    </h3>
    </main>

  <div class="container">
  <form action="action_page.php">


    <h9>
    <label for= "fname" >First Name</label>
    <input type="text" id="fname" name="firstname" placeholder="Your name...>

    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lastname" placeholder="Your last name..">

    </h9>

    <label for="country">Country</label>
    <select id="country" name="country">
      <option value="australia">Australia</option>
      <option value="canada">Canada</option>
      <option value="usa">USA</option>
       <option value="China">China</option>
       <option value="India">India</option>
       <option value="Indonesia">Indonesia</option>
       <option value="Mexico">Mexico</option>
      
    </select>
<h9>
    <label for="subject">Subject</label>
    <textarea id="subject" name="subject" placeholder="Write something.." style="height:200px"></textarea>
</h9>
      
    <input type="submit" value="Submit">

  </form>
</div>



</body>

</html>
