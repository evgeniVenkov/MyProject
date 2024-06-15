<template>
 <h1>article vue</h1>
<div class="articles">
  <div v-for = "el in articles" :key="el.id">
    <h2>{{el.name}}</h2>
    <p>{{el.title}}</p>
  </div>
</div>

</template>

<script>
export default {

  data() {
    return {
      articles:[{
        id : 1,
        name : "Name one",
        title : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam, velit!",
      },
      {
        id : 2,
        name : "Name two",
        title : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam, velit!",
      },
      {
        id : 3,
        name : "Name three",
        title : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam, velit!",
      },
      {
        id : 4,
        name : "Name four",
        title : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam, velit!",
      },]
    }
  },
  methods:{

  }
}
</script>

<style scoped>

</style>