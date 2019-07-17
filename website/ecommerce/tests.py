# from django.test import TestCase
#
# # Create your tests here.
# <!--
# {% block signup %}
#
# {% load i18n widget_tweaks %}
# <div class="modal-dialog  modal-lg" >
#
# <form method="post" id="news-create" class="form" > {% csrf_token %}
#      <div class="modal-content">
#
#     <div class="modal-header">
#
#         <h4 class="modal-title">SIGN UP</h4>
#           <button class="close" data-dismiss="modal-dialog" >&times;</button>
#             </div>
#          <br><br>
#
#
#          <div class="modal-body">
#
#     <input type="text" name="username" class="form-control" maxlength="150" placeholder="Username" autofocus="" required="" id="id_username" style="font-size:130%;padding:2% 3% 2% 3%;">
#
#     <br><br>
#
#     <input type="email" name="email" class="form-control" maxlength="50" placeholder="Email" required="" id="id_email" style="font-size:130%;padding:2% 3% 2% 3%;">
#
#     <br><br>
#
#     <input type="password" name="password1" class="form-control" placeholder="Password" required="" id="id_password1" style="font-size:130%;padding:2% 3% 2% 3%;">
#
#     <br><br>
#
#
#     <input type="password" name="password2" class="form-control" placeholder="Confirm Password" required="" id="id_password2" style="font-size:130%%;padding:2% 3% 3% 2%;">
#
#     <br>
#          </div>
#           <div class="modal-footer">
#     <button type="submit" style="margin-left:150px;background-color:white; font-size:16px; padding:10px; border-radius:20px; cursor:pointer;">SIGN UP</button>
#
#           </div>
#          </div>
# </form>
# </div>
#
# <script>
#     var form_options = { target: '#modal', success: function(response) {} };
#        $('#news-create').ajaxForm(form_options);
# </script>
#
#
# <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#
# {% endblock %}
# -->
#
# <!--
#
# <form method="post">
#     {% csrf_token %}
#     {{ form }}
#     <input type="submit" value="Submit">
# </form>
#
# -->


#
# <ul>
#     {% recursetree genres %}
#         <li>
#             {{ node.name }}
#             {% if not node.is_leaf_node %}
#                 <ul class="children">
#                     {{ children }}
#                 </ul>
#             {% endif %}
#         </li>
#     {% endrecursetree %}
# </ul>