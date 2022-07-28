"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlists"

    def __repr__(self):
        p = self
        return f"<Playlist name={p.name}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    name = db.Column(db.Text,
                        nullable=False)

    description = db.Column(db.Text,
                        nullable=False)


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "songs"

    def __repr__(self):
        p = self
        return f"<Song title={p.title}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.Text,
                        nullable=False)

    artist = db.Column(db.Text,
                        nullable=False)

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlistsongs"

    def __repr__(self):
        p = self
        return f"<Playlist id={p.playlist_id} songid={p.songs_id}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    playlist_id = db.Column(db.Integer,
                        db.ForeignKey('playlists.id'))
    
    songs_id = db.Column(db.Integer,
                        db.ForeignKey('songs.id'))
    
    playlist = db.relationship('Playlist', backref='playlistofsongs')
    song = db.relationship('Song', backref='playlistofsongs')

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
