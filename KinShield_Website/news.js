// api url 
const api_url = 
	"https://newsapi.org/v2/top-headlines?country=us&category=health&q=covid&pageSize=5&apiKey=862442c555f5480699aa12c8e3744cd5"; 

// Defining async function 
async function getapi(url) { 
	
	// Storing response 
	const response = await fetch(url); 
	
	// Storing data in form of JSON 
	var data = await response.json(); 
	console.log("HERE"+data); 
	if (response) { 
		//hideloader(); 
	} 
	show(data); 
} 
// Calling that async function 
getapi(api_url); 

// Function to hide the loader 
function hideloader() { 
	document.getElementById('loading').style.display = 'none'; 
} 
// Function to define innerHTML for HTML table 
function show(data) { 
	let tab = 
		`      <div class="container" data-aos="zoom-in">

        <div class="testimonials-slider swiper-container" data-aos="fade-up" data-aos-delay="100">
          <div class="swiper-wrapper">`; 
	
	// Loop to access all rows 
	for (let r of data.articles) { 
		tab += ` <div class="swiper-slide">
              <div class="testimonial-item">
                <img src="assets/img/testimonials/testimonials-1.jpg" class="testimonial-img" alt="">
                <h3>${r.url}</h3>
                <h4>${r.title}</h4>
                <p>
                  <i class="bx bxs-quote-alt-left quote-icon-left"></i>
                 ${r.description}
                  <i class="bx bxs-quote-alt-right quote-icon-right"></i>
                </p>
              </div>
            </div>`; 
	} 
	tab += `    </div>
          <div class="swiper-pagination"></div>
        </div>

      </div>`;
	// Setting innerHTML as tab variable 
	document.getElementById("testimonials").innerHTML = tab; 
} 
