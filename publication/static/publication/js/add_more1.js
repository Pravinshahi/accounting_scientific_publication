
        $(document).ready(function() {
        var max_fields_limit      = 10; //set limit for maximum input fields
        var x = 1; //initialize counter for text box
             var data = [{'1':'Name'}, {'2': 'Age'}];
             var html = "";
              for(var key in obj) {
            html += "<option selected value=" + key  + ">" +obj[key] + "</option>"
        }
              console.log(html)

        $('.add_more_button').click(function(e){ //click event on add more fields button having class add_more_button
            e.preventDefault();
            if(x < max_fields_limit){ //check conditions
                x++; //counter increment
                $('.input_fields_container').append('<div>' +
                    '<select id="RequestType" class="form-control" name="id_status" id="id_status">'+
                        html +
                    ' </select>'+
                    '<a href="#" class="remove_field" style="margin-left:10px;">Удалить</a></div>'); //add input field
            }
        });
        $('.input_fields_container').on("click",".remove_field", function(e){ //user click on remove text links
            e.preventDefault(); $(this).parent('div').remove(); x--;
        })
    });


