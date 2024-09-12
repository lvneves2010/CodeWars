function rgb(r, g, b) {
  let rex = r < 256 ? r.toString(16).padStart(2, '0').toUpperCase() : "FF";
  let gex = g < 256 ? g.toString(16).padStart(2, '0').toUpperCase() : "FF";
  let bex = b < 256 ? b.toString(16).padStart(2, '0').toUpperCase() : "FF";
  if( r < 0 ) rex = "00";
  if( g < 0 ) gex = "00";
  if( b < 0 ) bex = "00";
  
  let rgbex = (rex + gex + bex).toString();
    return rgbex;
}