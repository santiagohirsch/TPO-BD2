db.albums.find().forEach(function(album) {
    var rank = album.Number;
    var score = 501 - rank;
    db.albums.updateOne(
        { _id: album._id },
        { $set: { score: score } }
    );
});