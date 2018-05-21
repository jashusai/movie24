#!/usr/bin/env python
import webbrowser
import os
import re
print("Content-type:text/html \n")


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html>
<head>

    <meta name="viewport" content="width=device-width,initial-scale=1.0">

    <title>Movie trailers</title>



   <style>
   .modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top:100px;
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content/Box */
.modal-content {
    margin: 5% auto; /* 5% from the top and centered */
    padding: 20px;
    width: 560px; /* Could be more or less, depending on screen size */
    min-height:500px;
}

/* The Close Button */
.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    background-color: black;
    text-decoration: none;
    cursor: pointer;
    padding-left:5px;
    padding-right:5px;
}

      .container{
        display: flex;
        flex-wrap:wrap;
        font-family:arial,cursive;
       background-color : #000000;
       }
     .box{
          width:100%;
          min-height:150px;
        }
      @media screen and (min-width :450px)  {
      div.J1:hover{
      background-color:#778899;
             }
       div.J2:hover{
       background-color:#003333;
             }
       div.J3:hover{
       background-color :#999966;
       }
       div.J4:hover{
       background-color:#cccc00;
             }
       div.J5:hover{
       background-color:#336699;
             }
       .J1{width:50%;}
       .J2{width:50%;}
       .J3{width:50%;}
       .J4{width:50%;}
       .J5{width:50%;}
       h1 {background-color:black;}
        }
      h1 {background-color:#2F4F4F;
         font-family:arial,cursive;}
      </style>
      <div>
      <!-- The Modal -->
         <div id="myModal" class="modal" >

  <!-- Modal content -->
           <div class="modal-content">
                <span class="close">&times;</span>
                 <iframe id="f" width="560" height="315"
                                {movie_tiles
                                 src="" frameborder="0"
                                 allow="autoplay;
                                 encrypted-media"
                                 allowfullscreen>
                                 </iframe>
        </div>
        </div>
</div>
<script>
   // Get the modal
var modal = document.getElementById('myModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
    onc = function(c) {
    modal.style.display = "block";
    c='https://www.youtube.com/embed/'+c;
    console.log(c);
    document.getElementById("f").setAttribute("src",c);
}

// When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
}
span.onclick = function(){
            console.log("hello");
            var iframe = document.getElementById("f");
            iframe.src = iframe.src;
            modal.style.display = "none";
        }

// When the user clicks anywhere outside of the modal, close it
   window.onclick = function(event) {
       if (event.target == modal) {
          modal.style.display = "none";
    }
}
</script>

</head>
'''

# The main page layout and title bar
main_page_content = '''
<body style="text-align:center">
   <h1 style="color:white">MOVIE TRAILERS</h1>
   <div class="container">
   <div class="box J1"  onclick="onc('sueMmTm-M4Y')">
        <img vspace="10"src="https://bit.ly/2KHHLei"
        style="width:60%" height="300" hspace="20">
        </a><h4 style="color:#000000;">Rangastalam</h4></div>
   <div class="box J2"  onclick="onc('ZnVIUr_BQSs')">
        <img vspace="10" src="https://bit.ly/2KF6rUU"
        style="width:60%" height="300" hspace="20"></a>
        <h4 style="color:#000000;">Naa peru surya</h4></div>
   <div class="box J3"  onclick="onc('KMWS5y2gZ6E')">
        <img vspace="10" src="https://bit.ly/2ITtkXz"
        style="width:60%" height="300" hspace="20">
        </a><h4 style="color:#000000;">Bharat ane nenu</h4></div>
   <div class="box J4"  onclick="onc('6ZfuNTqbHE8')">
        <img vspace="10" src="https://bit.ly/2IztZOy"
        style="width:60%" height="300"
        hspace="20"></a><h4 style="color:#000000;">Avengers</h4></div>
   <div class="box J5"  onclick="onc('M8mCjRbCPIo')">
        <img vspace="10" src="https://bit.ly/2rWQLVt"
        style="width:60%" height="300"  hspace="20">
        </a><h4 style="color:#000000;">Ghajinikanth</h4></div>
</body>
</html>
'''

movie_tile_content = '''
<div class = "col-md-6 col-lg-4 movie-title text-center"
             data-trailer-youtbe-id="{trailer_youtube_id}"
             data-toggle="modal" data-target="#trailer">
     <img src="{poster_image_url}" width="220" height="342">
     <h2 style="color:white;">{movie_title}</h2>
    </div>
'''


def create_movie_tiles_content(movies):
    sai = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        sai += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
         )
        return sai


def open_movies_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_sai = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    output_file.write(main_page_head+rendered_sai)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)
