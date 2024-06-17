<script>

</script>

<template>
<header>
  <img src="/logo.svg" alt="">
  <ul>
    <li> <RouterLink to="/" active-class="active"> Главная</RouterLink> </li>
    <li><a href="">Товары</a></li>
    <li><RouterLink to="/delivery" active-class="active"> Доставка </RouterLink></li>
    <li><RouterLink to="/about" active-class="active"> Про нас</RouterLink></li>
    <li><img src="/basket.svg" alt=""></li>

  </ul>
</header>


</template>

<style scoped>
header{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 50px;
}
header ul{
  list-style: none;
}
header ul li {
  display: inline-block;
  margin-left: 25px;
  cursor: pointer;
}

.active{
  padding: 5px 15px;
  background: #B2BAC1;
  border-radius: 20px;
}
.active:hover{
  color:white;
  background: #616569;
}

header ul li a{
  position: relative;
  bottom: 10px;
}
</style>