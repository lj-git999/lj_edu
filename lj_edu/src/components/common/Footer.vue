<template>
    <div class="footer">
        <ul >
            <li v-for="(footer,index) in footer_list" :key="index">
                <span v-if="footer.is_site"><a :href="footer.link" class="foot">{{footer.title}}</a></span>
                <span v-else><a href="javascript:;" @click="foot(footer.link)" class="foot">{{footer.title}}</a></span>
            </li>
        </ul>
    </div>

</template>

<script>
export default {
    name: "Footer",
    data() {
        return {
            footer_list: [],
        }
    },
    methods: {
        get_footer() {
            this.$axios({
                url: this.$settings.HOST + "home/footer/",
                method: "get"
            }).then(rst => {
                console.log(rst.data);
                this.footer_list=rst.data;
            }).catch(error => {
                console.log(error);
            })
        },
        foot(link){
            console.log(link)
            this.$router.push({path:link});
        }
    },
    created() {
        this.get_footer();
    }
}
</script>

<style scoped>
.footer {
    width: 100%;
    height: 128px;
    background: #25292e;
    color: #fff;
}

.footer ul {
    margin: 0 auto 16px;
    padding-top: 38px;
    width: 810px;
}

.footer ul li {
    float: left;
    width: 112px;
    margin: 0 10px;
    text-align: center;
    font-size: 14px;
}

.footer ul::after {
    content: "";
    display: block;
    clear: both;
}

.footer p {
    text-align: center;
    font-size: 12px;
}
.foot{
    color: #ffc210;
}
</style>
