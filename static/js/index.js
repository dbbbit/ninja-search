$(function ($) {
    var q = $('#keyword'),
        local_default = [
            "ActionScript",
            "AppleScript",
            "Asp",
            "BASIC",
            "C",
            "C++",
            "Clojure",
            "COBOL",
            "ColdFusion",
            "Erlang",
            "Fortran",
            "Groovy",
            "Haskell",
            "Java",
            "JavaScript",
            "Lisp",
            "Perl",
            "PHP",
            "Python",
            "Ruby",
            "Scala",
            "Scheme",
            "测试",
            "v2ex"
        ],
        cache = {}

    var filter = function (array, searching_str) {
        return $.grep(array, function (value) {
            //关键字满足开头才返回,忽略大小写
            return 0 === value.toLowerCase().indexOf(searching_str.toLowerCase())
        })
    }

    q.autocomplete({
        source: function (rq, rsp) {
            var term = rq.term
            if (term in cache) {
                rsp(cache[term])
            }
            else {
                $.getJSON('/', rq)
                    //远程获取
                    .done(function (data) {
                        console.info('done')
                        cache[term] = data //缓存每次远程结果
                        rsp(data)
                    })
                    //远程失败则从本地获取
                    .fail(function (jq) {
                        console.info('fail')
                        rsp(filter(local_default, term))
                    })
            }
        }
    })
})
