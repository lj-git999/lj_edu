<template>
    <div id="app">
        <Header></Header>
        <Banner></Banner>
        <Footer></Footer>
        <router-view></router-view>
    </div>
</template>

<script>
import Footer from "./components/common/Footer";
import Banner from "./components/Banner";
import Header from "./components/common/Header";

export default {
    name: 'App',
    components:{
        Header:Header,
        Banner:Banner,
        Footer:Footer,


    }
}
</script>

<style>

</style>
