<?php
// POST 요청이 있을 경우
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // 데이터베이스 연결
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "pizza";

    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // 입력한 데이터 추출
    $ingredient1 = $_POST['source1'];
    $ingredient2 = $_POST['source2'];
    $ingredient3 = $_POST['source3'];
    $ingredient4 = $_POST['source4'];
    $ingredient5 = $_POST['source5'];
    $ratio1 = $_POST['source1_i'];
    $ratio2 = $_POST['source2_i'];
    $ratio3 = $_POST['source3_i'];
    $ratio4 = $_POST['source4_i'];
    $ratio5 = $_POST['source5_i'];

    // id가 1인 데이터가 있는지 확인
    $sql_check = "SELECT * FROM pie WHERE id=1";
    $result_check = mysqli_query($conn, $sql_check);

    if(mysqli_num_rows($result_check) > 0) {
      // id가 1인 데이터가 있을 경우, 업데이트
      $sql_update = "UPDATE pie SET source1='$ingredient1', source1_i='$ratio1', source2='$ingredient2', source2_i='$ratio2', source3='$ingredient3', source3_i='$ratio3', source4='$ingredient4', source4_i='$ratio4', source5='$ingredient5', source5_i='$ratio5' WHERE id=1";
      if (mysqli_query($conn, $sql_update)) {
          echo "Record updated successfully";
      }
  } else {
      // id가 1인 데이터가 없을 경우, 새로 입력
      $sql_insert = "INSERT INTO pie (id, source1, source1_i, source2, source2_i, source3, source3_i, source4, source4_i, source5, source5_i) VALUES (1, '$ingredient1', '$ratio1', '$ingredient2', '$ratio2', '$ingredient3', '$ratio3', '$ingredient4', '$ratio4', '$ingredient5', '$ratio5')";
      if (mysqli_query($conn, $sql_insert)) {
          echo "Record inserted successfully";
      }
  }
  
  // 데이터베이스 연결 종료
  mysqli_close($conn);
  
  // pie.php로 리다이렉트
  header("Location: pie.php");
  exit();
  
}
?>

<!-- HTML 폼 -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Pizza Ingredients</title>
  </head>
  <body>
    <form method="post">
      <label for="source1">재료 1:</label>
      <input type="text" id="source1" name="source1" required>
      <label for="source1_i">비율:</label>
      <input type="number" id="source1_i" name="source1_i" required><br>

      <label for="source2">재료 2:</label>
      <input type="text" id="source2" name="source2" required>
      <label for="source2_i">비율:</label>
      <input type="number" id="source2_i" name="source2_i" required><br>

      <label for="source3">재료 3:</label>
      <input type="text" id="source3" name="source3" required>
      <label for="source3_i">비율:</label>
      <input type="number" id="source3_i" name="source3_i" required><br>

      <label for="source4">재료 4:</label>
      <input type="text" id="source4" name="source4" required>
      <label for="source4_i">비율:</label>
      <input type="number" id="source4_i" name="source4_i" required><br>

      <label for="source5">재료 5:</label>
      <input type="text" id="source5" name="source5" required>
      <label for="source5_i">비율:</label>
      <input type="number" id="source5_i" name="source5_i" required><br>

      <button type="submit">입력</button>
    </form>
  </body>
</html>
