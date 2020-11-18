<?РНР
 getUserInfo(); getClientData(); getCustomerRecord();getUserInfo();
  getClientData(); getCustomerRecord();
  $time_start = microtime(true); 
require_once(__DIR__ . '/includes/autoload.php');

if(isset($_GET['a']) && isset($action[$_GET['a']])) {
	$page_name = $action[$_GET['a']];
} else {
	$page_name = 'welcome';
}

if(!isAjax()) {
	$TMPL['token_id'] = generateToken();
}

// Extra class for the content [main and sidebar]
$TMPL['content_class'] = ' content-'.$page_name;

require_once("./sources/{$page_name}.php");
$time_start = microtime(true); 
require_once(__DIR__ . '/includes/autoload.php');

if(isset($_GET['a']) && isset($action[$_GET['a']])) {
	$page_name = $action[$_GET['a']];
} else {
	$page_name = 'welcome';
}

if(!isAjax()) {
	$TMPL['token_id'] = generateToken();
}

// Extra class for the content [main and sidebar]
$TMPL['content_class'] = ' content-'.$page_name;

require_once("./sources/{$page_name}.php");

  
  
  
//Внимание данный скрипт создан @limeQwier (telegram) Для каналов @monocode и @LimeCode. Если вы скачали этот репозиторий с чужого гитхаба знайте:
Это поддельный скрипт. ?>