from CTFd import utils
from flask import render_template
from CTFd.plugins import (
	register_user_page_menu_bar,
	register_plugin_assets_directory
)

def load(app):
	#https://github.com/beatgammit/base64-js/blob/master/base64js.min.js
	#https://github.com/blueimp/JavaScript-MD5/blob/master/js/md5.min.js
	register_plugin_assets_directory(app, base_path='/plugins/hasher/assets/')

	register_user_page_menu_bar(name='Hasher', route='/hasher')

	@app.route('/hasher', methods=['GET'])
	def hash():
		return render_template('page.html', content="<script src='/themes/original/static/js/vendor/jquery.min.js' type='text/javascript'></script>"\
"<script src='/plugins/hasher/assets/md5.min.js' type='text/javascript'></script>"\
"<script src='/plugins/hasher/assets/base64js.min.js' type='text/javascript'></script>"\
"<script src='/plugins/hasher/assets/sha.js' type='text/javascript'></script>"\
"<h1>Hash a value</h1>"\
"<input id='valuetohash' style='width: 400px;'></input>"\
"<button id='hash'>go</button><br/>"\
"<label id='output'></label>"\
"<button id='copy'>copy</button>"\
"<script>"\
"    $(function() {"\
"        $('#hash').click( function()"\
"            {"\
"                var val = $('#valuetohash').val();\n"\
"                //var hash = md5(val);\n"\
"                var shaObj = new jsSHA('SHA-256', 'TEXT');\n"\
"                shaObj.update(val);\n"\
"                var hash = shaObj.getHash('HEX');"\
"                var b64str = base64js.fromByteArray(hash);"\
"                $('#output').html(b64str);"\
"            }"\
"        );"\
"  "\
"        $('#copy').click( function()"\
"            {"\
"                var $temp = $('<input>');"\
"                $('body').append($temp);"\
"                $temp.val($('#output').text()).select();"\
"                document.execCommand('copy');"\
"                $temp.remove();"\
"            }"\
"        );"\
"    });"\
"</script>")

	utils.hasher = hash
