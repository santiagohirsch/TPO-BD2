db.albums.aggregate([
    {
        $group: {
            _id: "$Artist",
            Score: { $sum: "$score" }
        }
    },
    {
        $sort: { Score: -1 }
    }
]).forEach(printjson);