/*
 *		This file contains the javascript code for our animals website
 */

// variables for all of the templates so we only have to compile
// them once on page load and can then use the same compiled 
// templates many times
var categories_template, species_template, animal_template, navbar_template;

var current_category = animals_data.categories[0];
var current_species = current_category.species[0];

// a helper function that instantiates a template
// and displays the results in the content div
function showTemplate(template, data){
	var html = template(data);
	$('#content').html(html);
}


// document read gets called when the whole document
// is loaded, so we put most of the code that needs to run
// in here
$(document).ready(function(){

	//
	// compile all of our templates ready for use
	//
	source   = $("#categories-template").html();
	categories_template = Handlebars.compile(source);
	
	source = $("#species-template").html();
	species_template = Handlebars.compile(source);
	
	source = $("#animal-template").html();
	animal_template = Handlebars.compile(source);


	// 
	//  clicking on the categories tab shows the 
	//  thumbnails of all the categories
	//
	$("#categories-tab").click(function () {

		
		// displays the categories template
		showTemplate(categories_template, animals_data);

		// make the categories tab the active one
		// first make the currently active tab inactive
		$(".nav-tabs .active").removeClass("active");
		// then make categories tab active
		$("#categories-tab").addClass("active");

		// add a click callback to each category 
		// thumbnail which displays the species
		// template on that category
		$(".category-thumbnail").click(function (){
			
			// get the index (position in the array)
			// of the category we clicked on
			// "this" is the element that was clicked on
			// data("id") gets the attribute data-id
			// (which we set to the index of the category in
			// the array - @index)
			var index = $(this).data("id");

			// set the current category to this category
			current_category = animals_data.categories[index];

			// displays the species template
			$("#species-tab").click();
		});
	});

	// 
	//  clicking on the species tab shows all of the 
	//  species in the current category
	//
	$("#species-tab").click(function () {
		
		// displays the species template
		showTemplate(species_template, current_category);

		current_species = current_category.species[0];

		$("#next-category").click(function () {
			next_category_index = animals_data.categories.indexOf(current_category) + 1
			if (next_category_index >= animals_data.categories.length) {
				next_category_index = 0
			}
			current_category = animals_data.categories[next_category_index]
			current_species = current_category.species[0];
			$("#species-tab").click();
		});

		$("#prev-category").click(function () {
			prev_category_index = animals_data.categories.indexOf(current_category) - 1
			if (prev_category_index < 0) {
				prev_category_index = animals_data.categories.length-1
			}
			current_category = animals_data.categories[prev_category_index]
			current_species = current_category.species[0];
			$("#species-tab").click();
		});

		// make the species tab the active one
		// first make the currently active tab inactive
		$(".nav-tabs .active").removeClass("active");
		// then make species tab active
		$("#species-tab").addClass("active");

		// add an on click al all the species thumbnails
		// which displays the species in a modal popup
		$(".species-thumbnail").click(function (){
			
			// get the index (position in the array)
			// of the species we clicked on
			// "this" is the element that was clicked on
			// data("id") gets the attribute data-id
			// (which we set to the index of the species in
			// the array - @index)
			var index = $(this).data("id");

			// set the current v to this species
			current_species = current_category.species[index];
			
			// displays the single species template
			$("#animal-tab").click();
		});
	});

	// 
	//  clicking on the animal tab displays the
	//  current animal 
	//
	$("#animal-tab").click(function () {

		// display the animal template using the 
		// current species
		showTemplate(animal_template, current_species);

		var category_name = document.getElementById("category_name");
		category_name.innerText = current_category.name

		$("#next-category").click(function () {
			next_category_index = animals_data.categories.indexOf(current_category) + 1
			if (next_category_index >= animals_data.categories.length) {
				next_category_index = 0
			}
			current_category = animals_data.categories[next_category_index]
			current_species = current_category.species[0];
			$("#animal-tab").click();
		});

		$("#prev-category").click(function () {
			prev_category_index = animals_data.categories.indexOf(current_category) - 1
			if (prev_category_index < 0) {
				prev_category_index = animals_data.categories.length-1
			}
			current_category = animals_data.categories[prev_category_index]
			current_species = current_category.species[0];
			$("#animal-tab").click();
		});

		$("#next-species").click(function () {
			next_species_index = current_category.species.indexOf(current_species) + 1
			if (next_species_index >= current_category.species.length) {
				next_species_index = 0
			}
			current_species = current_category.species[next_species_index]
			$("#animal-tab").click();
		});

		$("#prev-species").click(function () {
			prev_species_index = current_category.species.indexOf(current_species) - 1
			if (prev_species_index < 0) {
				prev_species_index = current_category.species.length-1
			}
			current_species = current_category.species[prev_species_index]
			$("#animal-tab").click();
		});

		
		// make the animal tab the active one
		// first make the currently active tab inactive
		$(".nav-tabs .active").removeClass("active");
		// then make animal tab active
		$("#animal-tab").addClass("active");
	});



	// start the page by showing the categories view
	// we do this by virtually clicking on the 
	// categories tab
	$("#categories-tab").click();

});