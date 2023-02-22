window.onscroll = function() {scrollFunction()};

var navbar = document.getElementById("banner_bottom");
var sticky = navbar.offsetTop;
var jobs = document.getElementsByClassName("job-title");
var input = document.getElementById("paperInput");
var table = document.getElementById("paperTable");

function scrollFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky_banner")
    navbar.classList.remove("non_sticky_banner")
  } else {
    navbar.classList.remove("sticky_banner")
    navbar.classList.add("non_sticky_banner");
  }
}



if (jobs) {
    var i;

    for (i = 0; i < jobs.length; i++) {
      jobs[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel
        this.classList.toggle("active"); */

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;

        if (panel.style.maxHeight) {
          panel.style.maxHeight = null;
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      });
    }
}

function searchFunction() {
// function that searchs table
    var filter, tr, td, i, j, txtValue;
    filter = input.value.toUpperCase();
    tr = table.getElementsByTagName("tr");
    for (i = 1; i < tr.length; i++) {
        data = tr[i].getElementsByTagName("td");

        if (data) {
            tr[i].style.display = "none";
            for (j = 0; j < data.length; j++) {
                td = data[j]
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
    	        }
            }
        }
    }
}

function sortTable(n) {
  /* A function that sorts the table in two directions depending on which one
  is already fulfilled, i.e. only sort for descending order if the table is
  sorted in ascending order. The argument is the table column to sort for */

  var rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;

  switching = true;
  /* Normally sort for ascending order, only sort for descending order if the
  table is sorted perfectly in ascending order, i.e. perfect is when no change
   is necessary*/
  dir = "asc";
  /*Make a loop that will continue until no switching has been done:*/
  while (switching) {
    // assume that no switching is necessary and only set to true later if
    // checked
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the first, which contains table
     headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      // no switching unless found to be otherwise later
      shouldSwitch = false;
      /*Get the two elements to compare */
      x = rows[i].getElementsByTagName("td")[n];
      y = rows[i + 1].getElementsByTagName("td")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch= true;
          /* breaking the loop keeps the i value intact at the index to be
           switched */
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch at the current index i
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /*If no switching has been done AND the direction is "asc", i.e. the table
      is perfectly sorted already, the only possible choice will be to sort it
      the other way, i.e. that is descending, so set the direction to "desc" and
      run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
  // get the header elements
  header = rows[0].getElementsByTagName("th");
  // get the active header that is being clicked on
  header_active = header[n];
  /*  To do list:
  - [x] get charcodes for both arrows
  - [x] check identity with charcode with Stringmethods
  - [x] remove if arrow present
  - [x] remove all other arrows in different columns
  - [] debate whether to use a different symbol (like wikipedia a triangle)
  - [] put the symbol at the end
  - [] use a neutral symbol

  */
  for (i=0; i < header.length; i++){
      header_element = header[i];
      lastindex = header_element.innerHTML.length-1;
      if (header_element.innerHTML.charCodeAt(lastindex) == 11015 ||
        header_element.innerHTML.charCodeAt(lastindex) == 11014 ||
        header_element.innerHTML.charCodeAt(lastindex) == 11021) {
            header_element.innerHTML =
                header_element.innerHTML.slice(0,lastindex);
        }
      if (i != n) {
          header_element.innerHTML =
            header_element.innerHTML + String.fromCharCode(11021);
          }

    }

        /* ⬍ is 11021 (both arrows)
           ⬆ is 11014 (arrow up)
           ⬇ is 11015 (arrow down)
        */
    // 8593 is charcode for up arrow
  // 8595 is charcode for down arrow

  if (dir == "asc") {
      header_active.innerHTML =
        header_active.innerHTML + String.fromCharCode(11015);
  } else if (dir = "desc") {
      header_active.innerHTML =
        header_active.innerHTML + String.fromCharCode(11014); ;
  }
}
