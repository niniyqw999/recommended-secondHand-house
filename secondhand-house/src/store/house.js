import {defineStore} from 'pinia'


const houseStore = defineStore('house',{
    state:()=>({
        tableData:[
              {
                name:'汉口小区',
                region:'武昌区',
                price:188,
                hostype:'3室1厅',
                size:120,
                direction:'东南',
                playtype:'精装',
                height:20,
                islike:false
              },
        ],
        searchData:[],
        regionOptions:[
            {label:'江岸区',value:'江岸区'},
            {label:'江汉区',value:'江汉区'},
            {label:'硚口区',value:'硚口区'},
            {label:'汉阳区',value:'汉阳区'},
            {label:'武昌区',value:'武昌区'},
            {label:'青山区',value:'青山区'},
            {label:'洪山区',value:'洪山区'},
            {label:'东西湖区',value:'东西湖区'},
            {label:'汉南区',value:'汉南区'},
            {label:'蔡甸区',value:'蔡甸区'},
            {label:'江夏区',value:'江夏区'},
            {label:'黄陂区',value:'黄陂区'},
            {label:'新洲区',value:'新洲区'}
        ],
        directionOptions:[
            {label:'东',value:'东'},
            {label:'南',value:'南'},
            {label:'西',value:'西'},
            {label:'北',value:'北'},
            {label:'东南',value:'东南'},
            {label:'东北',value:'东北'},
            {label:'西南',value:'西南'},
            {label:'西北',value:'西北'},
        ],
        hostypeOptions:[
            {label:'3室2厅',value:'3室2厅'},
            {label:'3室1厅',value:'3室1厅'},
            {label:'2室1厅',value:'2室1厅'},
            {label:'1室1厅',value:'1室1厅'},
        ]
    }),
    actions:{
      changeLike(name){
        let likeone = this.tableData.find(h=>h.name===name)
        if(likeone){
          likeone.islike=!likeone.islike
        }
      },
      search(form){
        this.searchData= this.tableData.filter(h =>(h.name===form.name||form.name==='') && (h.region===form.region||form.region==='') && (h.direction===form.direction||form.direction==='') && (h.hostype===form.hostype||form.hostype===''))
      }
    },
    getters:{

    }
})

export default houseStore