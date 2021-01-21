<template>
  <div>
    <el-carousel height="720px" :interval="3000" arrow="always">
      <el-carousel-item v-for="(banner,index) in banner_list" :key="index">
        <a :href="banner.link"><img :src="banner.img" alt=""></a>
      </el-carousel-item>
    </el-carousel>
  </div>


</template>

<script>
export default {
  name: "Banner",
  methods:{
    get_banner(){
      this.$axios({
        url:this.$settings.HOST+"home/banner/",
        method:"get",
      }).then(rst=>{
        console.log(rst.data);
        this.banner_list=rst.data

      }).catch(error=>{
        console.log(error);
      })
    }
  },
  created() {
    this.get_banner();
  },
  data(){
    return{
      banner_list:[],
    }
  }
}
</script>

<style scoped>
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6;
}
</style>
