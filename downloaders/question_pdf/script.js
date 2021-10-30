const ARROW_D = "M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"
let HEIGHT_LIMITOR_XPATH = '//*[@id="root"]/div/div[6]'
let WIDTH_LIMITOR_XPATH = '//*[@id="root"]/div/div[6]/div[6]/div/div'
let ELEMENTS_TO_REMOVE = [
    '//*[@id="root"]/div/div[6]/div[6]/div/div[3]', // Elements to the right of the Vertical separator
    '//*[@id="root"]/div/div[6]/div[6]/div/div[2]', // Vertical separator
    '//*[@id="root"]/div/div[6]/div[6]/div/div/div/div[3]', // horizontal bar
    '//*[@id="root"]/div/div[6]/div[6]/div/div/div/div[2]', // element under bar
]

removeHeightWidthLimit()
removeElementsByXpath(ELEMENTS_TO_REMOVE)
fixButtons()
expand_questions_and_solution_walkthroughs()


function expand_questions_and_solution_walkthroughs(){
    for (let ele of findElementsByXpath('//*[@tabindex]')){
        if (ele.nodeName === "DIV"){
            let contains_svg = ele.querySelector(`path[d="${ARROW_D}"]`)
            if (contains_svg) {ele.querySelector('div').click()}
        }
    }
}


function removeHeightWidthLimit(){
    let height_limitor = findElementByXpath(HEIGHT_LIMITOR_XPATH)
    height_limitor.style.height = 'auto'
    let width_limitor = findElementByXpath(WIDTH_LIMITOR_XPATH)
    width_limitor.style.flex = ''
}

function removeElementsByXpath(path_list){
    for (let path of path_list){
        let element = findElementByXpath(path)
        element.remove()
    }
}

function fixButtons(){
    let buttons = findElementsByXpath('//*[@id="root"]/div/div[6]/div[6]/div/div/div/div/div/div[1]/button')
    for (let i=0; i<buttons.length; i++){
        buttons[i].style.height='auto'
    }
}

// Reference to the medium article about Xpath
// https://developer.mozilla.org/en-US/docs/Web/XPath/Introduction_to_using_XPath_in_JavaScript
function findElementsByXpath(expression, contextNode=document, namespaceResolver=null, resultType=XPathResult.ANY_TYPE, result=null){
    let xpathResult = document.evaluate(expression, contextNode, namespaceResolver, resultType, result)
    let nodes = []
    while (true){
        let node = xpathResult.iterateNext()
        if (node === null) break
        nodes.push(node)
    }
    return nodes
}

function findElementByXpath(expression, contextNode=document, namespaceResolver=null, resultType=XPathResult.FIRST_ORDERED_NODE_TYPE, result=null){
    let xpathResult = document.evaluate(expression, contextNode, namespaceResolver, resultType, result)
    return xpathResult.singleNodeValue
}
