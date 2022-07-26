// 柱状图1模块
(function() {
    // 实例化对象
    var myChart = echarts.init(document.querySelector(".bar .chart"));
    // 指定配置和数据
    var option = {
        color: ["#2f89cf"],
        tooltip: {
            trigger: "axis",
            axisPointer: {
                // 坐标轴指示器，坐标轴触发有效
                type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        grid: {
            left: "0%",
            top: "10px",
            right: "0%",
            bottom: "4%",
            containLabel: true
        },
        xAxis: [{
            type: "category",
            data: [
                "旅游行业",
                "教育培训",
                "游戏行业",
                "医疗行业",
                "电商行业",
                "社交行业",
                "金融行业"
            ],
            axisTick: {
                alignWithLabel: true
            },
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: "12"
                }
            },
            axisLine: {
                show: false
            }
        }],
        yAxis: [{
            type: "value",
            axisLabel: {
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: "12"
                }
            },
            axisLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)"
                    // width: 1,
                    // type: "solid"
                }
            },
            splitLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)"
                }
            }
        }],
        series: [{
            name: "直接访问",
            type: "bar",
            barWidth: "35%",
            data: [200, 300, 300, 900, 1500, 1200, 600],
            itemStyle: {
                barBorderRadius: 5
            }
        }]
    };

    // 把配置给实例对象
    myChart.setOption(option);
    window.addEventListener("resize", function() {
        myChart.resize();
    });

    // 数据变化
    var dataAll = [{
            year: "2019",
            data: [200, 300, 300, 900, 1500, 1200, 600]
        },
        {
            year: "2020",
            data: [300, 400, 350, 800, 1800, 1400, 700]
        }
    ];

    document.querySelector(".bar h2").addEventListener("click", function(e) {
        var i = e.target == this.children[0] ? 0 : 1;
        option.series[0].data = dataAll[i].data;
        myChart.setOption(option);
    });
})();



// 饼形图定制
(function() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector(".pie .chart"));

    option = {
        tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b}: {c} ({d}%)",
            position: function(p) {
                //其中p为当前鼠标的位置
                return [p[0] + 10, p[1] - 10];
            }
        },
        legend: {
            top: "90%",
            itemWidth: 10,
            itemHeight: 10,
            data: ["0岁以下", "20-29岁", "30-39岁", "40-49岁", "50岁以上"],
            textStyle: {
                color: "rgba(255,255,255,.5)",
                fontSize: "12"
            }
        },
        series: [{
            name: "年龄分布",
            type: "pie",
            center: ["50%", "42%"],
            radius: ["40%", "60%"],
            color: [
                "#065aab",
                "#066eab",
                "#0682ab",
                "#0696ab",
                "#06a0ab",
                "#06b4ab",
                "#06c8ab",
                "#06dcab",
                "#06f0ab"
            ],
            label: {
                show: false
            },
            labelLine: {
                show: false
            },
            data: [{
                    value: 1,
                    name: "0岁以下"
                },
                {
                    value: 4,
                    name: "20-29岁"
                },
                {
                    value: 2,
                    name: "30-39岁"
                },
                {
                    value: 2,
                    name: "40-49岁"
                },
                {
                    value: 1,
                    name: "50岁以上"
                }
            ]
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function() {
        myChart.resize();
    });
})();
// 学习进度柱状图模块
(function() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.querySelector(".bar1 .chart"));

    var data = [90, 80, 75, 65, 65];
    var titlename = ["Java", "PHP", "GO", "HTML5", "VUE"];
    var valdata = ["精通", "熟练", "熟练", "掌握", "掌握"];
    var myColor = ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#8B78F6"];
    option = {
        //图标位置
        grid: {
            top: "10%",
            left: "22%",
            bottom: "10%"
        },
        xAxis: {
            show: false
        },
        yAxis: [{
                show: true,
                data: titlename,
                inverse: true,
                axisLine: {
                    show: false
                },
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: false
                },
                axisLabel: {
                    color: "#fff",

                    rich: {
                        lg: {
                            backgroundColor: "#339911",
                            color: "#fff",
                            borderRadius: 15,
                            // padding: 5,
                            align: "center",
                            width: 15,
                            height: 15
                        }
                    }
                }
            },
            {
                show: true,
                inverse: true,
                data: valdata,
                axisLabel: {
                    textStyle: {
                        fontSize: 12,
                        color: "#fff"
                    }
                }
            }
        ],
        series: [{
                name: "条",
                type: "bar",
                yAxisIndex: 0,
                data: data,
                barCategoryGap: 50,
                barWidth: 10,
                itemStyle: {
                    normal: {
                        barBorderRadius: 20,
                        color: function(params) {
                            var num = myColor.length;
                            return myColor[params.dataIndex % num];
                        }
                    }
                },
                label: {
                    normal: {
                        show: true,
                        position: "inside",
                        formatter: "{c}%"
                    }
                }
            },
            {
                name: "框",
                type: "bar",
                yAxisIndex: 1,
                barCategoryGap: 50,
                data: [100, 100, 100, 100, 100],
                barWidth: 15,
                itemStyle: {
                    normal: {
                        color: "none",
                        borderColor: "#00c1de",
                        borderWidth: 3,
                        barBorderRadius: 15
                    }
                }
            }
        ]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function() {
        myChart.resize();
    });
})();


// 点位分布统计模块
(function() {
    // 1. 实例化对象
    var myChart = echarts.init(document.querySelector(".pie1  .chart"));
    // 2. 指定配置项和数据
    var option = {
        legend: {
            top: "90%",
            itemWidth: 10,
            itemHeight: 10,
            textStyle: {
                color: "rgba(255,255,255,.5)",
                fontSize: "12"
            }
        },
        tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        // 注意颜色写的位置
        color: [
            "#006cff",
            "#60cda0",
            "#ed8884",
            "#ff9f7f",
            "#0096ff",
            "#9fe6b8",
            "#32c5e9",
            "#1d9dff"
        ],
        series: [{
            name: "点位统计",
            type: "pie",
            // 如果radius是百分比则必须加引号
            radius: ["10%", "70%"],
            center: ["50%", "42%"],
            roseType: "radius",
            data: [{
                    value: 20,
                    name: "西安"
                },
                {
                    value: 26,
                    name: "北京"
                },
                {
                    value: 24,
                    name: "上海"
                },
                {
                    value: 25,
                    name: "其他"
                },
                {
                    value: 20,
                    name: "武汉"
                },
                {
                    value: 25,
                    name: "杭州"
                },
                {
                    value: 30,
                    name: "深圳"
                },
                {
                    value: 42,
                    name: "广州"
                }
            ],
            // 修饰饼形图文字相关的样式 label对象
            label: {
                fontSize: 10
            },
            // 修饰引导线样式
            labelLine: {
                // 连接到图形的线长度
                length: 10,
                // 连接到文字的线长度
                length2: 10
            }
        }]
    };

    // 3. 配置项和数据给我们的实例化对象
    myChart.setOption(option);
    // 4. 当我们浏览器缩放的时候，图表也等比例缩放
    window.addEventListener("resize", function() {
        // 让我们的图表调用 resize这个方法
        myChart.resize();
    });
})();