var RF_PLAYER_INITIALIZED = false;
var RF_PLAYER_OFFLINE = false;
var ACTUAL_PLAYING_TRACK = false;
var ACTUAL_SCHEDULE = '';

var playingSchedules = [];

function updatePlayerDataElement()
{
    if (playingSchedules.length > 0) {
        ACTUAL_SCHEDULE = playingSchedules[playingSchedules.length - 1].schedule;
    } else {
        ACTUAL_SCHEDULE = '';
    }

    var playing = ACTUAL_SCHEDULE;

    if (PLAYER_SHOW_MUSIC_NAME) {
        if (ACTUAL_PLAYING_TRACK) {
            if (playing != '') {
                playing += ' - <strong>Tocando agora: ' + ACTUAL_PLAYING_TRACK + '</strong>';
            } else {
                playing = 'Tocando agora: ' + ACTUAL_PLAYING_TRACK;
            }
        }
    }

    if ($('.rf-player .rf-playing-now marquee').length == 0) {
        $('.rf-player .rf-playing-now').html('<marquee></marquee>');
    }

    $('.rf-player .rf-playing-now marquee').html(playing);
}

var RfPlayer = new function() {
    var $this = this;

    this.volume = 1.0;
    this.playing = false;
    this.audioSource = '';

    this.playerElement = null;
    this.playerSource = null;
    this.playButton = null;
    this.pauseButton = null;
    this.volumeAreaElement = null;
    this.volumeMeterElement = null;

    this.initialize = function(params) {

        $.each(NEXT_SCHEDULES, function (i, e) {
            setTimeout(function() {
                playingSchedules.push(e);
                updatePlayerDataElement();
            }, e.start * 1000);

            setTimeout(function() {
                $.each(playingSchedules, function(j, r) {
                    if (typeof r !== 'undefined' && r.id == e.id) {
                        playingSchedules.splice(j, 1);
                    }
                });
                updatePlayerDataElement();
            }, e.end * 1000);
        });

        $this.audioSource = params.audioSource;

        if (!$this.hasAudioSupport()) {
            $this.flashFallback();
            return;
        }

        $this.playerElement = $('#rf-player');

        if ($this.playerElement[0].canPlayType(params.streamType) == '') {
            $this.flashFallback();
            return;
        }

        $this.playerSource = $this.playerElement.find('source').first();
        $this.playButton = $('#rf-player-play');
        $this.pauseButton = $('#rf-player-pause');
        $this.volumeAreaElement = $('#rf-player-volume-area');
        $this.volumeMeterElement = $('#rf-player-volume-meter');

        $this.volumeMeterElement.css({'width' : parseInt($this.volumeAreaElement[0].offsetWidth) + 'px'});

        $this.playButton.on('click', $this.play);
        $this.pauseButton.on('click', $this.pause);
        $this.volumeAreaElement.on('click', $this.changeVolumeByClicking);
        $this.playerElement.on('error', $this.audioSourceError);

        if (PLAYER_AUTOSTART && !IS_MOBILE) {
            $this.play();
        }
    };

    this.play = function() {
        $this.playing = true;
        $this.playerSource[0].src = $this.audioSource;
        $this.playerElement[0].load();
        $this.playerElement[0].play();

        $this.pauseButton.addClass('active');
        $this.playButton.removeClass('active');
    };

    this.pause = function() {
        $this.playing = false;
        $this.playerSource[0].src = '';
        $this.playerElement[0].load();
        $this.playerElement[0].pause();

        $this.pauseButton.removeClass('active');
        $this.playButton.addClass('active');
    };

    this.changeVolumeByClicking = function(event) {
        var width = event.clientX - $this.volumeAreaElement.offset().left;
        if (width > 0) {
            $this.volumeMeterElement.css({'width' : width + 'px'});
            $this.volume = (width / $this.volumeAreaElement.width());

            $this.playerElement[0].volume = $this.volume;
        }
    };

    this.hasAudioSupport = function() {
        return !!(document.createElement('audio').canPlayType);
    };

    this.audioSourceError = function() {
        if ($this.playing) {
            $this.flashFallback();
        }
    }

    this.flashFallback = function() {
        var flashVars = {
            'file' : $this.audioSource + '?type=.flv',
            'provider' :'http',
            'http.startparam' : 'starttime',
            'autostart' : PLAYER_AUTOSTART && !IS_MOBILE,
            'icons' : false,
            'skin' : BASE_ASSETS + 'players/' + PLAYER_ID + '/skin.zip',
            'start' : 1,
            'duration' : '-1',
            'bufferlength' : '5',
            'scale' : 'exactFit'
        };

        swfobject.embedSWF(BASE_ASSETS + 'players/player.swf',
            'rf-player-container',
            '100%',
            '100%',
            '9.0.115',
            'false',
            flashVars,
            { allowfullscreen : 'true', allowscriptaccess : 'always', wmode : 'transparent' },
            { id : 'jwplayer', name : 'jwplayer' },
            function (e) {
                if (!e.success) {
                    console.log('NÃ£o compatÃ­vel');
                }
            }
        );
    };

    this.refreshPlayerData = function() {

        var defaultRefreshInterval = 30000;

        if (BRLOGIC_STREAMING && $('.rf-player').length && !RF_PLAYER_OFFLINE) {
            var refreshInterval = defaultRefreshInterval;

            var targetUrl = 'http://cdn-api-streaming.brlogic.com/index.php/api/unsafeget/allstatus/' + STREAMING_PORT + '/' + PLAYER_AUTH_HASH + '/' + STREAMING_ADDRESS_ONLY;
            if (typeof USE_PLAYER_PROXY !== 'undefined' && USE_PLAYER_PROXY) {
                targetUrl = '/player/proxy?address=' + STREAMING_ADDRESS_ONLY + '&port=' + STREAMING_PORT;
            }

            $.ajax({
                url: targetUrl,
                dataType: 'json',
                success: function(data) {

                    IS_MOBILE = data.isMobile;

                    if (!RF_PLAYER_INITIALIZED && data.streamingStatus == 1) {
                        RfPlayer.initialize({
                            'audioSource' : STREAMING_ADDRESS,
                            'streamType' : data.streamingType
                        });

                        RF_PLAYER_INITIALIZED = true;
                    }

                    if (data.streamingStatus == 0) {
                        RF_PLAYER_OFFLINE = true;
                        $('.rf-player-container').html('<img class="offline-image" src="' + BASE_ASSETS + 'img/website/streaming-offline.png" />');
                    } else {

                        ACTUAL_PLAYING_TRACK = data.currentTrack;

                        if (!PLAYER_SHOW_MUSIC_NAME) {
                            refreshInterval = 600000;
                        }

                        updatePlayerDataElement();

                        setTimeout($this.refreshPlayerData, refreshInterval);
                    }
                },
                error: function() {
                    setTimeout($this.refreshPlayerData, refreshInterval);
                }
            });
        }
    }
};

$(document).ready(function() {
    RfPlayer.refreshPlayerData();

    if (!BRLOGIC_STREAMING && !RF_PLAYER_INITIALIZED) {
        RfPlayer.initialize({
            'audioSource' : STREAMING_ADDRESS,
            'streamType' : STREAMING_TYPE
        });

        if ($('.rf-player .rf-playing-now marquee').length == 0) {
            $('.rf-player .rf-playing-now').html('<marquee></marquee>');
        }
        $('.rf-player .rf-playing-now marquee').html(ACTUAL_SCHEDULE);

        RF_PLAYER_INITIALIZED = true;
    }
});
