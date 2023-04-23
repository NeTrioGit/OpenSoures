<?php
// 데이터베이스 연결
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "pizza";

$conn = mysqli_connect($servername, $username, $password, $dbname);

// 데이터베이스에서 데이터 가져오기
$sql = "SELECT * FROM pie";
$result = mysqli_query($conn, $sql);

// 데이터 배열 생성
$data = array();
while($row = mysqli_fetch_assoc($result)) {
  $data[] = array($row['source1'], (int)$row['source1_i']);
  $data[] = array($row['source2'], (int)$row['source2_i']);
  $data[] = array($row['source3'], (int)$row['source3_i']);
  $data[] = array($row['source4'], (int)$row['source4_i']);
  $data[] = array($row['source5'], (int)$row['source5_i']);
}

// 데이터 배열을 JSON 형태로 변환
$json_data = json_encode($data);

// Google Charts 로드
echo '<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>';
echo '<script type="text/javascript">';
echo "google.charts.load('current', {'packages':['corechart']});";
echo "google.charts.setOnLoadCallback(drawChart);";

// 차트 출력 함수
echo "function drawChart() {";
echo "var data = google.visualization.arrayToDataTable(" . $json_data . ");";
echo "var options = { title: 'Pizza making' };";
echo "var chart = new google.visualization.PieChart(document.getElementById('piechart'));";
echo "chart.draw(data, options);";
echo "}";
echo "</script>";

// 차트 출력
echo "<div id='piechart' style='width: 900px; height: 500px;'></div>";

// 데이터베이스 연결 종료
mysqli_close($conn);
?>
