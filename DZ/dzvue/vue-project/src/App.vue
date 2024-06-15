
<template>
<h1 v-on:click="changetext">{{ title }}</h1>
  <p @mouseover="changetext">{{ !is_cat }}</p>
  <p>{{info}}</p>
  <input @input="textDual($event.target.value)" type="text" />
  <p v-bind:style="style">Simple Text</p>
  <input @input = styletext($event.target.value) type="text"/>
  <br>
  <br>
  <button @click="this.is_show=!this.is_show">click</button>
  <h1 v-if="is_show">text show</h1>
  <br><br><br>

  <ul>
    <li v-for="(el,index) in book" v-bind:key="index">
      {{index+1}} - {{el.name}} / <b>{{el.autor}}</b> = {{el.genre}}
    </li>
  </ul>

</template>

<script>
export default {
  data(){
    return{
      title:"Text title",
      is_cat: false,
      userInput: '',
      style: '',
      is_show:true,
      book:[
          {name:"Hitman",autor:"Evgen",genre:"Boevik!"},
          {name:"Krovati",autor:"Igor",genre:"Roman!"},
          {name:"Martishka",autor:"Mandarin",genre:"History!"},
      ],
    };
  },
  methods: {
    changetext () {
      this.title = "new";
    },
    textDual (val) {
      this.userInput = val;
    },
    styletext(val){
      this.style = val
    },
  },
  computed:{
    info(){
      if (this.userInput === '')return ''
      return "text:" + this.userInput
    },
  },
};
</script>

<style>

</style>
