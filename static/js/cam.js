var axiom=['FFFF++FFF++F++FF--FF--FF++F++FFF ++++ffff-- FFFF++FFF++FFFF++F++F--F--F++F++ff++fF--F--F--F ff--fff-- FFFF++FFFFF++FFFF++F++FFF--F--FFF++F++FFF--F--FFF++F']; /*
letter E=='FFFFF++FFF++F++FF--F--FF++F++FF--F--FF++F++FFF'  
letter C=='FFFF++FFF++F++FF--FF--FF++F++FFF'
letter L=='FFFF++F++FFF--FF++F++FFF' 
letter R=='FFFF++FFR++FFR++++F--F--F++F++ff++fF--F--F--F' 
letter T=='FFF--F++F++FFF++F++F--FFF++F'   
letter F==='FFFFF++FFF++F++FF--F--FF++F++FF--FF++F' 
Letter A=='FFFF++FFF++FFFF++F++F--F--F++F++ff++fF--F--F--F'
Letter A=='FFFF++FFF++FFFF++F++F--F--F++F++ff++fF--F--F--F'*/

var alphabet=[['F','f','E','R','+','-','[',']'],['F','f','E','R','+','-','[',']'],['F','f','E','R','+','-','[',']'],['F','f','E','R','+','-','[',']'],['F','f','E','R','+','-','[',']'],['F','f','E','R','+','-','[',']'],['F','f','E','R','+','-','[',']']];
var successor_alphabet=[['F++F[++F]--F[++F][F]--F++FF','ffff','E','R++R[++R]--R[++R][R]--R++RR','+','-','[',']'],['F++F[++F]--F[++F][F]--F++FF','ffff','E','R++R[++R]--R[++R][R]--R++RR','+','-','[',']'],['F++F[++F]--F[++F][F]--F++FF','ffff','E','R++R[++R]--R[++R][R]--R++RR','+','-','[',']'],['F++F[++F]--F[++F][F]--F++FF','ffff','E','R++R[++R]--R[++R][R]--R++RR','+','-','[',']'],['F++F[++F]--F[++F][F]--F++FF','ffff','E','R++R[++R]--R[++R][R]--R++RR','+','-','[',']'],['F++F[++F]--F[++F][F]--F++FF','ffff','E','R++R[++R]--R[++R][R]--R++RR','+','-','[',']'],['F++F[++F]--F[++F][F]--F++FF','ffff','E','R++R[++R]--R[++R][R]--R++RR','+','-','[',']']];
var sentence=axiom;
var index=0;

var angle=180;
var n_of_interactions=0;
var control= false;
var translation= false;
var run=false;
var run=false;
var minusrun=false;
var click_color=false;
var last_sentence=axiom;
var weight=5;
var delta=1;
var width_canvas=screen.width*0.95;
var height_canvas=width_canvas*0.4;
var len=(height_canvas*0.15);
var x=2.5*(width_canvas*0.08);
var y=5*len;
var i_color;
var j_color;

function setup(){
    angleMode(DEGREES);
    cnv=createCanvas(width_canvas,height_canvas);
    translate(width/2,height);
  
    
    cnv.mousePressed(click_canvas);
    


    var run_button=createButton('run');
    run_button.mousePressed(run_function);
    
    turtle();
    interact();
}
function draw(){
    textSize(15);
    stroke(color("#9f0000"));
    strokeWeight(1);
    if (control){
        angle=map(mouseX,0,1100,0,360);
        turtle();
    }   
    if(run){
        
        if (angle%(2.5*90)==0){
            angle=45
            run=false
        
        }
        else{
            angle+=delta;
        }


        turtle();
    }
    else if(minusrun){
        angle-=delta;
        turtle();
    }
    if (click_color){
        i_color=map(mouseX,0,width_canvas,0,360);
        j_color=map(mouseY,0,height_canvas,0,100);
        turtle();
   }
}
function control_color(){
    if(click_color){
        click_color=false;
    }
    else{
        click_color=true;
    }
}
function minusrun_function() {
    if (minusrun){
        minusrun=false;
    }
    else{
        minusrun=true;
        run=false;
    }
    
}
function next_function(){
    if(index<axiom.length){
        index+=1
        turtle();
    }
    else{
        index=0
        turtle();
    }
}
function run_function() {
    if (run){
        run=false;
    }
    else{
        run=true;
        minusrun=false;
}}
function click_canvas(){
    if (control){
        control_mouse();
    }
    else if (translation){
        translate_origin();
    }
    else if (click_color){
        control_color();
    }
    turtle();
}
function minusangle(){
    angle-=delta;
    turtle();
}
function plusangle(){
    angle+=delta;
    turtle();
}
function minus_delta(){
    delta=delta/10;
    turtle();
}
function plus_delta(){
    delta=10*delta;
    turtle();
}

function saveimg(){
    save('myCanvas.png');
}
function plus_px(){
    weight+=1;
    turtle();
}

function minus_px(){
    weight-=1;
    turtle();
}
function plus_angle(){
    weight+=1;
    turtle();
}
function plus_zoom(){
    len=len*(1.1)
    turtle();
}
function minus_zoom(){
    len=len*(0.9)
    turtle();
}
function control_mouse(){
    if (control){
        control=false;
    }
    else{
        control=true;
    }
}
function turtle(){
    
    clear();
    background(0);
    resetMatrix();
    translate(x,y);
    strokeWeight(weight);
    for(var i=0;i<sentence[index].length;i++){
        var char=sentence[index].charAt(i);
        if (char=='F'||char=='X'){
            colorMode(HSB);
            stroke(i_color,j_color,100);
            line(0,0,0,-len);
            translate(0,-len);
            
        }
        if (char=='f'){
            
            translate(0,-len);
        }
        if(char=='+'){
            rotate(angle);
        }
        if(char=='-'){
            rotate(-angle);
        }
        if(char=='['){
            push();
        }
        if(char==']'){
            pop();
        }
    
    }
    
}
function interact(){
    len=len/4;
    n_of_interactions++;
    last_sentence=sentence[index];
    var next_sentence='';
    for (var i=0; i<sentence[index].length; i++){
        var char=sentence[index].charAt(i);
        for(var j=0;j<alphabet[index].length;j++){
            if(char==alphabet[index][j]){
                next_sentence+=successor_alphabet[index][j];
            }
        }
    }
    
    sentence[index]=next_sentence;
    turtle();
    /*createP(sentence);*/
}

function translate_origin(){
    if (translation){
        x= mouseX;
        y= mouseY;
        turtle();
        translation=false;
    }
    else{
        translation=true;
    }
}
function translatex_minus_origin(){
    x-=delta;
    turtle();
}
function translatex_plus_origin(){
    x+=delta;
    turtle();
}
function translatey_minus_origin(){
    y-=delta;
    turtle();
}
function translatey_plus_origin(){
    y+=delta;
    turtle();
}