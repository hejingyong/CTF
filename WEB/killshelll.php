<?php//条件竞争
while (1) {
	$pid=1234;
	@unlink('./demo.php');
	exec('kill -9 $pid');
}
?>