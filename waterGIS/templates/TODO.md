Set up strong password requirements on login so that they need to have:
An upper case letter
A lower case letter
A number
A symbol
Be 10 characters long
Create a toggle button to display wells from “AnalytesSel.geojson” based on new fields that I will give you in the next update. Those fields will be:
d.properties.household
d.properties.livestock
d.properties.irrigation
d.properties.avoid
The values in each of those properties will be either 0 or 1. If a user clicks on the button to show wells from “household” it will display only wells where d.properties.household == 1.

 

Right now, the wells are displayed and colored based on the function getColor(wUse) in main.js – we will need to change this in the update since I do not want to symbolize wells using the field d.properties.USE.

----
Great news! I finished the ML algorithm to classify wells. I still need some time formatting the JS/JSON so that the popup boxes work correctly. In the meantime, I noticed a minor problem with the website that I hope you can fix.

 

You created the dropdown menu to zoom to individual chapters from `nnChapters.GEOjson`. It works perfectly (thank you!), BUT there are a lot of missing entries. There are 110 chapters in the Navajo Nation but only 60 in the dropdown menu. Also, they are out of alphabetical order. Will you please take some time to:

 

Include every chapter in the dropdown menu
Arrange them so that they are in alphabetical order?
 

This means that all code that looks like this:

    // NN Layers

    var chapter1Marker = L.marker([35.854359, -111.596276]);

    var chapter2Marker = L.marker([36.295128, -111.617351]);

    var chapter3Marker = L.marker([36.573259, -111.454201]);

needs to go to all the way to chaper110Marker, and that it needs to correspond with this code:

var chapterBounds = {

        'Cameron': L.latLngBounds([chapter1Marker.getLatLng()]),

        'Bodaway Gap': L.latLngBounds([chapter2Marker.getLatLng()]),

        'Coppermine': L.latLngBounds([chapter3Marker.getLatLng()]),

        'Tuba City': L.latLngBounds([chapter4Marker.getLatLng()]),

        'Coalmine Mesa': L.latLngBounds([chapter5Marker.getLatLng()]),

        'Leupp': L.latLngBounds([chapter6Marker.getLatLng()]),

In this order:

Alamo

Aneth

Baahaalii

Baca/Prewitt

Becenti

Beclahbito

Bird Springs

Black Mesa

Blue Gap/Tachee

Bodaway Gap

Burnham

Cameron

Casamero Lake

Chichiltah

Chilchinbeto

Chinle

Church Rock

City of Gallup

Coalmine Mesa

Coppermine

Cornfields

Counselor

Cove

Coyote Canyon

Crownpoint

Crystal

Dennehotso

Dilkon

Forest Lake

Fort Defiance

Gadiahai

Ganadp

Greasewood Springs

Hard Rock

Hogback

Houck

Huerfano

Indian Wells

Inscription House

Iyanbito

Jeddito

Kaibeto

Kayenta

Kinlichee

Klagetoh

Lake Valley

Lechee

Leupp

Littlewater

Low Mountain

Lukachukai

Lupton

Manuelito

Many Farms

Mariano Lake

Mexican Springs

Mexican Water

Nageezi

Nahat'a'dzil

Nahodishgish

Naschitti

Navajo Mountain

Nazlini

Newcomb

Oak Springs

Ojo Encino

Oljato

Pinedale

Pinon

Pueblo Pintado

Ramah

Red Lake

Red Mesa

Red Rock

Red Valley

Rock Point

Rock Springs

Rough Rock

Round Rock

Saint Michaels

San Juan/Nenahnezad

Sanostee

Sawmill

Sheep Springs

Shiprock

Shonto

Smith Lake

Standing Rock

Steamboat

Sweet Water

Teec Nos Pos

Teesto

Thoreau

Tohajilee

Tohatchi

Tolani Lake

Tonalea

Torreon

Tsaile/Wheatfields

Tsayatoh

Tselani

Tuba City

Twin Lakes

Two Grey Hills

Upper Fruitland

Whippoorwill

White Cone

Whitehorse Lake

Whiterock

Wide Ruins

 

This means that Alamo will correspond with chapter1Marker, and so on. Thank you, and please let me know if you have any questions. I’m going to New York next week so I probably won’t have the final JSON ready until next weekend. I’ll send that to you as soon as possible.
Hopefully I’ll have everything sorted soon. To recap, right now all well points are colored by d.properties.USE. That variable is gone in the new JSON. Instead, we have four new variables:

 

d.properties.Avoid

d.properties.Household

d.properties.Irrigation

d.properties.Livestock

 

Each variable only has a 0 or 1 value. I want to implement a radio button for each property that only draws wells where the value is 1. The default will be to draw every well, and I’d like a 5th button to show all wells. When you begin this task I will discuss with you the correct color codes and point properties.

 

I will rewrite the code to change the display in each popup.