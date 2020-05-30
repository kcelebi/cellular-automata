BufferedReader reader;
String line;
float x;
float y;

void setup(){
  background(0);
  size(1200,1020);
  String link = "/Users/kayacelebi/Projects/Cellular_Automata/1000x1000ca.txt";
  x = Integer.parseInt(link.split("/")[5].split("x")[0]);
  y = x;
  reader = createReader(link);
}

void draw(){
  int[][] mat = new int[(int)y][(int)x];
  int t = 0;
  while(t<y){
    try{
      line = reader.readLine();
    }
    catch(IOException e){
      line = null;
    }
    if(line == null)
    {
      noLoop();
    }
    else{
      String[] parsed = split(line,',');
      for(int p = 0; p < x; p++){
        mat[t][p] = Integer.parseInt(parsed[p]);
      }
      
      t++;
    }
  }
    for(int i=0; i < y; i++){
      for(int j=0; j < x; j++){
        fill(mat[i][j]*255);
        rect(i*width/x,j*height/y,width/x,height/y);
      }
    }
  
}
